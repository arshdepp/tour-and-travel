# Generated by Django 3.0.3 on 2020-05-25 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyo', '0012_waterparks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]