# Generated by Django 3.0.3 on 2020-04-30 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyo', '0004_carss'),
    ]

    operations = [
        migrations.CreateModel(
            name='flights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=30)),
                ('to', models.CharField(max_length=30)),
                ('depart', models.CharField(max_length=30)),
                ('Return', models.CharField(max_length=30)),
                ('Class', models.CharField(max_length=30)),
                ('adults', models.IntegerField()),
                ('child', models.IntegerField()),
            ],
        ),
    ]
