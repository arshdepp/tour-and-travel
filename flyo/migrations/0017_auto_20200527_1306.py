# Generated by Django 3.0.3 on 2020-05-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyo', '0016_auto_20200527_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewdetail',
            name='btn',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='btn1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='btn2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='btn3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='btn4',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='desc',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='desc1',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='desc2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='hdes',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='hotelname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='hotelplan',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='photo',
            field=models.ImageField(max_length=120, upload_to=''),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='photo2',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='photo3',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='photo4',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='pla',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='plan',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='plan2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='viewdetail',
            name='stay',
            field=models.CharField(max_length=100),
        ),
    ]
