# Generated by Django 2.0.1 on 2019-08-26 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_catetypeentity_fruitentity'),
    ]

    operations = [
        migrations.CreateModel(
            name='FruitImageEntty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(max_length=50, upload_to='', verbose_name='地址')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('fruit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.FruitEntity')),
            ],
            options={
                'verbose_name': '水果土图片',
                'verbose_name_plural': '水果土图片',
                'db_table': 't_fruit_image',
            },
        ),
        migrations.CreateModel(
            name='StoreEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='店名称')),
                ('boss_name', models.CharField(max_length=10, verbose_name='老板名称')),
                ('phone', models.CharField(max_length=10, verbose_name='电话')),
                ('address', models.CharField(max_length=50, verbose_name='具体地址')),
                ('city', models.CharField(max_length=20, verbose_name='城市')),
                ('lat', models.FloatField(verbose_name='纬度')),
                ('lon', models.FloatField(verbose_name='经度')),
            ],
            options={
                'verbose_name': '商店表',
                'verbose_name_plural': '商店表',
                'db_table': 't_store',
            },
        ),
        migrations.AlterModelOptions(
            name='catetypeentity',
            options={'ordering': ['-order_num'], 'verbose_name': '水果分类表', 'verbose_name_plural': '水果分类表'},
        ),
    ]
