from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Sum, Min, Max, Avg, F
from mainapp.models import UserEntity, FruitEntity, FruitImageEntty, StoreEntity
from django.conf import settings

# Create your views here.
def user_list(request):
    users = [
        {
            'id': 101,
            'name': 'tomas'
        },
        {
            'id': 102,
            'name': 'ben'
        },
        {
            'id': 103,
            'name': 'toni'
        }
    ]

    return render(request, 'user/list.html', locals())


def user_list2(request):
    users = UserEntity.objects.all()
    return render(request, 'user/list.html', locals())


def add_user(request):
    name = request.GET.get('name', default=None)
    age = request.GET.get('age', default=0)
    phone = request.GET.get('phone', default=None)
    # 验证数据是否完整
    if all((name, age, phone)):
        UserEntity(name=name, age=age, phone=phone).save()
    else:
        return HttpResponse('<h3 style="color:red;">用户信息不完整！</h3>', status=400)
    return redirect('/user/list2/')


def user_update(request):
    # 查询参数有id， name, phone
    # 通过模型查询id用户是否存在，Model类.objects.get()可能会出现异常 -- 尝试捕获
    id = request.GET.get('id', default=0)
    name = request.GET.get('name', default=None)
    age = request.GET.get('age', default=0)
    phone = request.GET.get('phone', default=None)
    if id and any((name, age, phone)):
        try:
            u = UserEntity.objects.get(pk=int(id))
        except Exception as e:
            return HttpResponse('<h3 style="color:red;">用户不存在！</h3>')
        if name:
            u.name = name
        if phone:
            u.phone = phone
        if age:
            u.age = age
        u.save()
        return redirect('/user/list2/')
    else:
        return HttpResponse('<h3 style="color:red;">参数不完整！</h3>', status=400)


def user_delete(request):
    # 查询参数有id
    # 验证id是否存在
    id = request.GET.get('id', default=0)
    if not id:
        return HttpResponse('<h3 style="color:red;">参数不完整！</h3>', status=400)
    try:
        u = UserEntity.objects.get(pk=int(id))
    except:
        return HttpResponse('<h3 style="color:red;">用户不存在！</h3>')
    u.delete()
    return redirect('/user/list2/')


def get_fruit_all(request):
    data = []
    fruits = FruitEntity.objects.all()
    for f in fruits:
        for img in FruitImageEntty.objects.all():
            print(f.name, img.fruit_id, f.id == img.fruit_id.id)
            if f.id == img.fruit_id.id:
                data.append({
                    'fruit': f,
                    'img': img
                })
                break
    print(data)
    return render(request, 'fruit/index.html', locals())


def find_fruit(request):
    # 从查询参数中获取价格区间price1, price2
    price1 = request.GET.get('price1', 0)
    price2 = request.GET.get('price2', 1000)
    # 根据价格区间查询满足条件所有水果信息
    # result = FruitEntity.objects.filter(price__gte=price1, price__lte=price2).exclude(price=250).filter(
    #     name__contains='果').all()
    data = []
    result = FruitEntity.objects.filter(price__gte=price1, price__lte=price2).all()

    for f in result:
        img = f.fruitimageentty_set.all()
        data.append({
            'fruit':f,
            'img':img[0] if img else ''
        })

    MEDIA = settings.MEDIA_URL
    # 将查询到的数据渲染到html模板中
    return render(request, 'fruit/index.html', locals())


def find_store(request):
    # 查询2019年开业的水果店
    # 查询参数：year, month
    queryset = StoreEntity.objects.filter(create_time__month__lte=3).order_by('-id', 'create_time')
    first_store = queryset.first() # 模型类的实例对象
    stores = queryset.all().filter(city='西安')

    return render(request, 'store/list.html', locals())


def all_store(request):
    # 返回所有水果店的json数据
    result = {}
    if StoreEntity.objects.exists():
        datas = StoreEntity.objects.values()
        print(type(datas)) # QuerySet<{},{}>
        print(datas)
        total = StoreEntity.objects.count()

        store_list = []
        for store in datas:
            store_list.append(store)
            # store_dict = {}
            # store_dict['id'] = store.id
            # store_dict['name'] = store.name
            # store_dict['city'] = store.city
            # store_list.append(store_dict)
        result['data'] = store_list
    else:
        result['mg'] = '数据为空'

    return JsonResponse(result)


def count_fruit(request):
    # 返回JSON数据：统计每种分类的水果数量、最高价格、最低价格和水果总价格
    # result = FruitEntity.objects.aggregate(cnt=Count('name'), max=Max('price'), min=Min('price'), avg=Avg('price'), sum=Sum('price'))
    result = StoreEntity.objects.filter(create_time=F('last_time')).values()
    data = {
        'data':[]
    }
    for r in result:
        data['data'].append(r)
    FruitEntity.objects.filter(id=10).update(price=F('price')+1)
    return JsonResponse(data)


def delete_fruit(request):
    # 使用QuerySet的delete方法删除数据
    name = request.GET.get('name')
    FruitEntity.objects.filter(name=name).delete()
    return redirect('../find/')