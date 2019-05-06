"""Model mixin for automatic atomic numbering of various JobBOSS entities"""
from django.db import models, transaction


class AutoNumberMixin(models.Model):
    class Meta:
        abstract = True

    def save_with_autonumber(self, *args, **kwargs):
        assert hasattr(self, 'auto_number_attrs'), \
            'Model class must have `auto_number_attrs` attribute to use ' \
            'AutoNumberMixin'
        assert isinstance(self.auto_number_attrs, dict), \
            '`auto_number_attrs` must be a dictionary'
        ana: dict = self.auto_number_attrs
        from jobboss.models import AutoNumber
        for attr_name, row in ana.items():
            if not getattr(self, attr_name):
                qs = AutoNumber.objects.select_for_update().filter(type=row)
                with transaction.atomic():
                    an_row: AutoNumber = qs.first()
                    setattr(self, attr_name, str(int(an_row.last_nbr) + 1))
                    self.save(*args, **kwargs)
                    an_row.last_nbr = str(int(an_row.last_nbr) + 1)
                    an_row.save()
            else:
                self.save(*args, **kwargs)
