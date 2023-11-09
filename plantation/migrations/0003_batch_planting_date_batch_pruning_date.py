# Generated by Django 4.2.7 on 2023-11-09 20:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantation', '0002_batch_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='planting_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 9, 20, 12, 29, 927929), verbose_name='Fecha de plantación'),
        ),
        migrations.AddField(
            model_name='batch',
            name='pruning_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de poda'),
        ),
    ]
