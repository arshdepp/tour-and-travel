# Generated by Django 3.0.3 on 2020-05-27 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flyo', '0017_auto_20200527_1306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viewdetail',
            old_name='name',
            new_name='name_of_destination',
        ),
    ]