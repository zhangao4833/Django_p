# Generated by Django 2.0.1 on 2019-08-29 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20190829_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentity',
            name='pwd',
            field=models.CharField(default=1, max_length=32, verbose_name='密码'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fruitentity',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fruits', to='mainapp.CateTypeEntity', verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='fruitentity',
            name='tags',
            field=models.ManyToManyField(blank=True, db_table='t_fruit_tag', related_name='fruits', to='mainapp.TagEntity', verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='fruitentity',
            name='users',
            field=models.ManyToManyField(blank=True, db_table='t_collect', related_name='fruits', to='mainapp.UserEntity', verbose_name='收藏用户列表'),
        ),
    ]
