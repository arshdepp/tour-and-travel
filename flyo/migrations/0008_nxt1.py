# Generated by Django 3.0.3 on 2020-05-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyo', '0007_trainn'),
    ]

    operations = [
        migrations.CreateModel(
            name='nxt1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=40)),
                ('berth_choice', models.CharField(max_length=30)),
            ],
        ),
    ]