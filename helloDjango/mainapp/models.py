import uuid

from django.db import models


# Create your models here.
class UserEntity(models.Model):
    name = models.CharField(max_length=20, verbose_name='账号')
    age = models.IntegerField(default=0, verbose_name='年龄')
    pwd = models.CharField(max_length=32,verbose_name='密码')
    phone = models.CharField(max_length=11, verbose_name='手机号', blank=True, null=True)

    class Meta:
        # 设置表名
        db_table = 't_user'
        verbose_name = '客户管理'
        # 设置复数表示方式
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 水果分类
class CateTypeEntity(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名')
    order_num = models.IntegerField(verbose_name='排序')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_category'
        ordering = ['-order_num']  # 指定排序字段 - 表示降序  默认升序
        verbose_name = '水果分类表'
        verbose_name_plural = verbose_name


class StoreEntity(models.Model):
    # 默认情况下，模型自创建主键id字段--隐式
    # 但是也可以显式的方式声明主键（primary_key）
    id = models.UUIDField(primary_key=True, verbose_name='店号')
    name = models.CharField(max_length=30, verbose_name='店名称')
    store_type = models.IntegerField(choices=((0, '自营'), (1, '第三方')), db_column='type_', verbose_name='店类型')

    boss_name = models.CharField(max_length=10, verbose_name='老板名称')
    phone = models.CharField(max_length=10, verbose_name='电话')
    address = models.CharField(max_length=50, verbose_name='具体地址')
    # 支持城市搜索, 所以创建索引
    city = models.CharField(max_length=20, db_index=True, verbose_name='城市')

    logo = models.ImageField(verbose_name='logo', upload_to='store', width_field='logo_width',
                             height_field='logo_height', null=True, blank=True)
    logo_width = models.IntegerField(verbose_name='logo宽', null=True)
    logo_height = models.IntegerField(verbose_name='logo高', null=True)

    summary = models.TextField(verbose_name='介绍', blank=True, null=True)

    opened = models.BooleanField(verbose_name='是否开业', default=False)

    create_time = models.DateField(verbose_name='成立时间', auto_now_add=True, null=True)
    last_time = models.DateField(verbose_name='最后变更时间', auto_now=True, null=True)

    # lat = models.FloatField(verbose_name='纬度')
    # lon = models.FloatField(verbose_name='经度')

    class Meta:
        # app_label = 'mainapp' # 指定当前模型的应用名称
        db_table = 't_store'
        verbose_name = '商店表'
        verbose_name_plural = verbose_name
        unique_together = (('name', 'city'),)

    def __str__(self):
        return self.name

    # 调用模型保存方法时调用

    @property
    def id_(self):
        return self.id.hex

    @property
    def open_time(self):
        print(self.create_time)
        return self.create_time

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.id:
            self.id = uuid.uuid4().hex
        super().save()


class FruitEntity(models.Model):
    name = models.CharField(max_length=20, verbose_name='水果名')
    price = models.FloatField(verbose_name='价格')
    source = models.CharField(max_length=30, verbose_name='原产地')
    category = models.ForeignKey(CateTypeEntity, related_name='fruits', on_delete=models.CASCADE, verbose_name='分类')
    store_id = models.ForeignKey(StoreEntity, on_delete=models.CASCADE)

    # 默认情况下，反向引用的名称是当前类的名称(小写）_ser
    # 可以通过related_name 来指定
    # db_table = 't_collect' 使用第三张表的方式建立fruit和user的多对多的关系
    users = models.ManyToManyField(UserEntity, db_table='t_collect', related_name='fruits', verbose_name='收藏用户列表', blank=True)
    tags = models.ManyToManyField('TagEntity', verbose_name='标签', db_table='t_fruit_tag',related_name='fruits', blank=True)

    class Meta:
        db_table = 't_fruit'
        verbose_name = '水果表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class FruitImageEntty(models.Model):
    fruit_id = models.OneToOneField(FruitEntity, on_delete=models.CASCADE, related_name='img')
    url = models.ImageField(upload_to='fruit', width_field='width', height_field='height', verbose_name='图片地址')
    width = models.IntegerField(verbose_name='宽')
    height = models.IntegerField(verbose_name='高')
    name = models.CharField(max_length=100, verbose_name='名称')

    class Meta:
        db_table = 't_fruit_image'
        verbose_name = '水果图片'
        verbose_name_plural = verbose_name
    #
    # def __str__(self):
    #     return self.fruit_id


class RealProfile(models.Model):
    # 声明一对一的关联关系
    user = models.OneToOneField(UserEntity, on_delete=models.CASCADE, verbose_name='登陆用户')
    real_name = models.CharField(max_length=20, verbose_name='真实姓名')
    number = models.CharField(max_length=30, verbose_name='证件号')
    real_type = models.IntegerField(choices=((0, '身份证'), (1, '护照'), (2, '驾驶证')), verbose_name='证件类型')

    image1 = models.ImageField(verbose_name='证件正面照', upload_to='user/real')
    image2 = models.ImageField(verbose_name='证件反面照', upload_to='user/real')

    class Meta:
        db_table = 't_user_profile'
        verbose_name_plural = verbose_name = '实名认证表'

    def __str__(self):
        return self.real_name



# 购物车
class CartEntity(models.Model):
    class Meta:
        db_table = 't_cart'
        verbose_name_plural = verbose_name = '购物车表'

    user = models.OneToOneField(UserEntity, on_delete=models.CASCADE, verbose_name='账号')
    no = models.CharField(primary_key=True, max_length=10, verbose_name='购物车编号')

    def __str__(self):
        return self.no


# 声明水果商品于购物车的关系表
class FruitCartEntity(models.Model):
    cart = models.ForeignKey(CartEntity, on_delete=models.CASCADE, verbose_name='购物车')
    fruits = models.ForeignKey(FruitEntity, on_delete=models.CASCADE, verbose_name='水果')
    cnt = models.IntegerField(verbose_name='数量')

    @property
    def price(self):
        # 属性方法在后台显示时没有verbose_name, 如何解决？
        return round(self.cnt * self.fruits.price, 2)

    @property
    def price1(self):
        # 属性方法在后台显示时没有verbose_name, 如何解决？
        return self.fruits.price  # 从获取主的属性

    class Meta:
        db_table = 't_fruit_cart'
        verbose_name_plural = verbose_name = '购物车详情表'

    def __str__(self):
        return self.fruits.name + '：' + self.cart.no


class TagEntity(models.Model):
    class Meta:
        db_table = 't_tag'
        verbose_name_plural = verbose_name = '标签表'
        ordering = ['-order_num']

    name = models.CharField(max_length=20, verbose_name='标签名', unique=True)
    order_num = models.IntegerField(verbose_name='标签序号', default=0)

    def __str__(self):
        return self.name