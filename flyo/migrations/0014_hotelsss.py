# Generated by Django 3.0.3 on 2020-05-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyo', '0013_auto_20200525_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotelsss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Picture', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('li1', models.TextField()),
                ('l12', models.TextField()),
                ('l13', models.TextField()),
                ('l14', models.TextField()),
                ('l15', models.TextField()),
            ],
        ),
    ]