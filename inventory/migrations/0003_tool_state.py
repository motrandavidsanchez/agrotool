# Generated by Django 4.2.7 on 2023-11-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_tool_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
