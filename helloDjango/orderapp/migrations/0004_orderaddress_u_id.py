# Generated by Django 2.0.1 on 2019-08-28 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_fruitcartentity'),
        ('orderapp', '0003_auto_20190828_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderaddress',
            name='u_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.UserEntity', verbose_name='所属用户'),
            preserve_default=False,
        ),
    ]
