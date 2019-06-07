"""Model mixin for automatic atomic numbering of various JobBOSS entities.

In addition to autonumber primary keys, JobBOSS has two other styles of
autonumbered columns:

1. "AutoNumber" entities where the last used number is stored in the JobBOSS
Auto_Number table, with a row for each type of entity. We call this
"AutoNumberColumn".

2. Secondary autonumber columns where a column other than the primary key has
an auto incremented unique integer. We call this "AutoIncrementColumn".
"""
from django.db import models, transaction
from django.db.models import Max


class AutoNumberMixin(models.Model):
    class Meta:
        abstract = True

    def save_with_autonumber(self, *args, **kwargs):
        assert hasattr(self, 'auto_number_attrs'), \
            'Model class must have `auto_number_attrs` attribute to use ' \
            'AutoNumberMixin'
        with transaction.atomic():
            auto_type: AutoColumnType
            for auto_type in self.auto_number_attrs:
                if not getattr(self, auto_type.attr_name):
                    auto_type.set_column(self)
            self.save(*args, **kwargs)


class AutoColumnType:
    def __init__(self, attr_name):
        self.attr_name = attr_name

    def set_column(self, record):
        raise NotImplemented


class AutoNumberColumn(AutoColumnType):
    def __init__(self, attr_name, jb_name):
        super().__init__(attr_name)
        self.jb_name = jb_name

    def set_column(self, record):
        from jobboss.models import AutoNumber
        qs = AutoNumber.objects.select_for_update().filter(type=self.jb_name)
        an_row: AutoNumber = qs.first()
        setattr(record, self.attr_name, str(int(an_row.last_nbr) + 1))
        an_row.last_nbr = str(int(an_row.last_nbr) + 1)
        an_row.save()


class AutoIncrementColumn(AutoColumnType):
    def set_column(self, record):
        manager = record.__class__.objects
        max_value = manager.select_for_update().all().aggregate(
            Max(self.attr_name))['{}__max'.format(self.attr_name)] or 0
        setattr(record, self.attr_name, max_value + 1)
