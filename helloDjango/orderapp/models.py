from django.db import models
from django.db.models import Q
from mainapp.models import FruitEntity, UserEntity


class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    last_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        abstract = True  # 抽象的模型类，即不会创建表


# 声明QuerySet或Manage的子类
class OrderManage(models.Manager):
    # 获取查询结果集对象QuerySet
    def get_queryset(self):
        return super().get_queryset().filter(~Q(pay_status=5))


class OrderAddress(models.Model):
    class Meta:
        db_table = 'order_address'
        verbose_name_plural = verbose_name = '收货地址表'

    u_id = models.ForeignKey(UserEntity, on_delete=models.CASCADE, verbose_name='所属用户')
    receiver = models.CharField(max_length=20, verbose_name='收货人')
    receiver_phone = models.CharField(max_length=11, verbose_name='收货人手机')
    receiver_address = models.TextField(verbose_name='收货地址')

    def __str__(self):
        return self.receiver_address


# Create your models here.

class OrderModel(models.Model):
    num = models.CharField(max_length=20, primary_key=True, verbose_name='订单号')
    title = models.CharField(max_length=100, verbose_name='订单名称')

    user_id = models.ForeignKey(UserEntity, on_delete=models.CASCADE, verbose_name='用户')
    address = models.ForeignKey(OrderAddress, on_delete=models.CASCADE, verbose_name='收货地址')

    class Meta:
        db_table = 't_order'
        verbose_name_plural = verbose_name = '订单表'

    def __str__(self):
        return self.title


class OrderPart(BaseModel):
    class Meta:
        db_table = 't_order_part'
        verbose_name_plural = verbose_name = '订单详情表'

    num_id = models.ForeignKey(OrderModel, verbose_name='订单', on_delete=models.CASCADE)
    goods_id = models.ForeignKey(FruitEntity, verbose_name='水果', on_delete=models.CASCADE)
    cnt = models.IntegerField(verbose_name='数量')

    pay_type = models.IntegerField(choices=((0, '余额支付'), (1, '银行卡支付'),
                                            (2, '微信支付'), (3, '支付宝支付')), verbose_name='支付方式', default=0)
    pay_status = models.IntegerField(choices=((0, '待支付'), (1, '已支付'), (2, '待收货'),
                                              (3, '已收货'), (4, '完成'), (5, '取消')), verbose_name='订单状态', default=0)


    objects = OrderManage()

    def __str__(self):
        return self.num_id.title

    @property
    def price(self):
        return self.goods_id.price

    @property
    def price1(self):
        return self.goods_id.price * self.cnt
