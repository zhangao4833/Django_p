# Generated by Django 2.0.1 on 2019-08-28 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='receiver_phone',
            field=models.CharField(max_length=11, verbose_name='收货人手机'),
        ),
    ]
