# Generated by Django 2.0.1 on 2019-08-29 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0005_remove_orderpart_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.UserEntity', verbose_name='用户'),
        ),
    ]