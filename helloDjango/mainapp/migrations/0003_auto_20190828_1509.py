# Generated by Django 2.0.1 on 2019-08-28 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190828_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeentity',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='电话'),
        ),
    ]
