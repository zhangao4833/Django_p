from django.contrib import admin
from mainapp.models import UserEntity, CateTypeEntity, FruitEntity, StoreEntity, FruitImageEntty, RealProfile, \
    CartEntity, FruitCartEntity
# Register your models here.
import xadmin


class UserAdmin(object):
    list_display = ('id', 'name', 'age', 'phone')
    list_per_page = 3
    list_filter = ('id', 'age')
    search_fields = ('id', 'phone')


class CateTypeAdmin(object):
    list_display = ('id', 'name', 'order_num')


class FruitAdmin(object):
    list_display = ('id', 'name', 'source', 'price', 'category')


class StoreAdmin(object):
    # readonly_fields = ('id',)
    list_display = (
        'id_', 'name', 'boss_name', 'city', 'phone', 'create_time', 'address', 'store_type', 'logo', 'opened')
    # 指定表单修改的字段
    fields = ('name', 'boss_name', 'city', 'phone', 'address', 'store_type', 'logo', 'summary', 'opened')


class FruitImageAdmin(object):
    # readonly_fields = ('fruit_id',)
    list_display = ('id', 'fruit_id', 'url', 'name')
    fields = ('fruit_id', 'url')


class RealProfileAdmin(object):
    list_display = ('user', 'real_name', 'number', 'real_type')


class CartEntityAdmin(object):
    list_display = ('user', 'no')


class FruitCartAdmin(object):
    list_display = ('cart', 'fruits', 'get_price1', 'cnt', 'get_price')

    def get_price1(self, obj):
        return obj.price1

    get_price1.short_description = '单价'

    def get_price(self, obj):
        return obj.price

    get_price.short_description = '小计'


xadmin.site.register(UserEntity, UserAdmin)
xadmin.site.register(CateTypeEntity, CateTypeAdmin)
xadmin.site.register(FruitEntity, FruitAdmin)
xadmin.site.register(FruitImageEntty, FruitImageAdmin)
xadmin.site.register(StoreEntity, StoreAdmin)
xadmin.site.register(RealProfile, RealProfileAdmin)
xadmin.site.register(CartEntity, CartEntityAdmin)
xadmin.site.register(FruitCartEntity, FruitCartAdmin)
