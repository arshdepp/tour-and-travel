# Generated by Django 3.0.3 on 2020-04-30 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyo', '0003_remove_hotels_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='carss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('pickup_location', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('pickup_date', models.CharField(max_length=10)),
                ('hours', models.IntegerField()),
                ('mins', models.IntegerField()),
                ('ampm', models.CharField(max_length=10)),
            ],
        ),
    ]
