import csv
from django.core import serializers
import json


def export_table(model_class, csv_filename):
    """Export an entire database table to a CSV file."""
    def flatten(row_dict):
        d = dict(pk=row_dict['pk'])
        d.update(**row_dict['fields'])
        return d

    qs = model_class.objects.all()
    first_row = qs.first()
    if not first_row:
        print('No rows in table')
        return
    header = flatten(json.loads(
        serializers.serialize('json', [first_row]))[0]).keys()
    with open(csv_filename, 'w') as f:
        dw = csv.DictWriter(f, header)
        dw.writeheader()
        for model_instance in qs:
            row = flatten(json.loads(
                serializers.serialize('json', [model_instance]))[0])
            dw.writerow(row)
