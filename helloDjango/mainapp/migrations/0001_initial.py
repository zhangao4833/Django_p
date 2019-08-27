# Generated by Django 2.0.1 on 2019-08-27 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CateTypeEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名')),
                ('order_num', models.IntegerField(verbose_name='排序')),
            ],
            options={
                'verbose_name': '水果分类表',
                'verbose_name_plural': '水果分类表',
                'db_table': 't_category',
                'ordering': ['-order_num'],
            },
        ),
        migrations.CreateModel(
            name='FruitEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='水果名')),
                ('price', models.FloatField(verbose_name='价格')),
                ('source', models.CharField(max_length=30, verbose_name='原产地')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.CateTypeEntity')),
            ],
            options={
                'verbose_name': '水果表',
                'verbose_name_plural': '水果表',
                'db_table': 't_fruit',
            },
        ),
        migrations.CreateModel(
            name='FruitImageEntty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(height_field='height', upload_to='fruit', verbose_name='图片地址', width_field='width')),
                ('width', models.IntegerField(verbose_name='宽')),
                ('height', models.IntegerField(verbose_name='高')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('fruit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.FruitEntity')),
            ],
            options={
                'verbose_name': '水果图片',
                'verbose_name_plural': '水果图片',
                'db_table': 't_fruit_image',
            },
        ),
        migrations.CreateModel(
            name='StoreEntity',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, verbose_name='店号')),
                ('name', models.CharField(max_length=30, verbose_name='店名称')),
                ('store_type', models.IntegerField(choices=[(0, '自营'), (1, '第三方')], db_column='type_', verbose_name='店类型')),
                ('boss_name', models.CharField(max_length=10, verbose_name='老板名称')),
                ('phone', models.CharField(max_length=10, verbose_name='电话')),
                ('address', models.CharField(max_length=50, verbose_name='具体地址')),
                ('city', models.CharField(db_index=True, max_length=20, verbose_name='城市')),
                ('logo', models.ImageField(blank=True, height_field='logo_height', null=True, upload_to='store', verbose_name='logo', width_field='logo_width')),
                ('logo_width', models.IntegerField(null=True, verbose_name='logo宽')),
                ('logo_height', models.IntegerField(null=True, verbose_name='logo高')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='介绍')),
                ('opened', models.BooleanField(default=False, verbose_name='是否开业')),
                ('create_time', models.DateField(auto_now_add=True, null=True, verbose_name='成立时间')),
                ('last_time', models.DateField(auto_now=True, null=True, verbose_name='最后变更时间')),
            ],
            options={
                'verbose_name': '商店表',
                'verbose_name_plural': '商店表',
                'db_table': 't_store',
            },
        ),
        migrations.CreateModel(
            name='UserEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='账号')),
                ('age', models.IntegerField(default=0, verbose_name='年龄')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号')),
            ],
            options={
                'verbose_name': '客户管理',
                'verbose_name_plural': '客户管理',
                'db_table': 't_user',
            },
        ),
        migrations.AlterUniqueTogether(
            name='storeentity',
            unique_together={('name', 'city')},
        ),
        migrations.AddField(
            model_name='fruitentity',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.StoreEntity'),
        ),
    ]
