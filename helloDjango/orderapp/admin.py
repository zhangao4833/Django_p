from django.contrib import admin
import xadmin
# Register your models here.
from orderapp.models import OrderModel, OrderAddress, OrderPart


class OrderAdmin(object):
    list_display = ('num', 'title', 'user_id', 'address')


class OrderAddressAdmin(object):
    list_display = ('receiver', 'receiver_phone', 'receiver_address')


class OrderPartAdmin(object):
    list_display = ('num_id', 'goods_id', 'cnt', 'get_price', 'get_price1', 'pay_type', 'pay_status')

    def get_price(self, obj):
        return obj.price

    get_price.short_description = '商品单价'

    def get_price1(self, obj):
        return obj.price1

    get_price1.short_description = '订单总价'


xadmin.site.register(OrderModel, OrderAdmin)
xadmin.site.register(OrderAddress, OrderAddressAdmin)
xadmin.site.register(OrderPart, OrderPartAdmin)
