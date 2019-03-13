import hashlib
import random

import time


from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow, FoodType, Goods, User, Cart


@cache_page(60*5)
def home(request):

    wheels = Wheel.objects.all()

    navs = Nav.objects.all()

    mustbuys = Mustbuy.objects.all()

    shops = Shop.objects.all()

    shophead = shops[0]
    shoptabs = shops[1:3]
    shopclasss = shops[3:7]
    shopcommends = shops[7:11]

    mainshows = Mainshow.objects.all()

    rensponse_dir = {
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptabs':shoptabs,
        'shopclasss':shopclasss,
        'shopcommends':shopcommends,
        'mainshows':mainshows,
    }

    return render(request,'home/home.html',context=rensponse_dir)


def market(request,childid='0',sortid='0'):
    try:
        foodtypes = cache.get('foodtypes')
        if foodtypes == None:
            raise Exception
    except:
        foodtypes = FoodType.objects.all()
        cache.set('foodtypes',foodtypes,60*60*24)
        foodtypes = cache.get('foodtypes')


    #goods_list = Goods.objects.all()[0:100]

    index = request.COOKIES.get('index','0')
    categoryid = foodtypes[int(index)].typeid

    if childid == '0':
        goods_list = Goods.objects.filter(categoryid=categoryid)
    else:
        goods_list = Goods.objects.filter(categoryid=categoryid).filter(childcid=childid)

    childtype_list = []

    for item in foodtypes[int(index)].childtypenames.split('#'):
        temp_dir = item.split(':')
        child_dir = {
            'childname':temp_dir[0],
            'id':temp_dir[1],
        }
        childtype_list.append(child_dir)

    if sortid == '1':
        goods_list = goods_list.order_by('-productnum')
    elif sortid == '2':
        goods_list = goods_list.order_by('price')
    elif sortid == '3':
        goods_list = goods_list.order_by('-price')



    rensponse_dir = {
        'foodtypes':foodtypes,
        'goods_list':goods_list,
        'childtype_list':childtype_list,
        'childid':childid,

    }

    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.get(pk=userid)
        cart_list = user.cart_set.all()
        rensponse_dir['cart_list'] = cart_list
    return render(request,'market/market.html',context=rensponse_dir)


def cart(request):
    token = request.session.get('token')
    userid = cache.get(token)
    if userid:
        user = User.objects.get(pk=userid)
        carts = Cart.objects.filter(user=user).filter(number__gt=0)

        isall = True
        for cart in carts:
            if not cart.isselect:
                isall = False


        response_dir = {
            'carts':carts,
            'isall':isall
        }

        return render(request, 'cart/cart.html',response_dir)
    else:
        return render(request,'mine/no_login.html')




def mine(request):
    token = request.session.get('token')
    userid = cache.get(token)
    user = None
    if userid:
        user = User.objects.get(pk=userid)
    return render(request,'mine/mine.html',context={'user':user})




def generate_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


def generate_token():
    temp = str(time.time()) + str(random.random)
    md5 = hashlib.md5()
    md5.update(temp.encode('utf-8'))
    return md5.hexdigest()


def register(request):
    if request.method == 'GET':
        return render(request, 'mine/register.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = generate_password(request.POST.get('password'))
        print(password)
        name = request.POST.get('name')

        user = User()
        user.email = email
        user.password = password
        user.name = name

        user.save()

        token = generate_token()
        request.session['token'] = token

        cache.set(token,user.id,60*2)



    return redirect('axf:mine')

def login(request):
    if request.method == 'GET':
        return render(request, 'mine/login.html')
    elif request.method == 'POST':
        email = request.POST.get('email')
        users = User.objects.filter(email=email)
        if users.exists():
            user = users.first()
            print(request.POST.get('password'))
            password = generate_password(request.POST.get('password'))
            if user.password == password:
                token = generate_token()

                cache.set(token,user.id,60*60*24*3)
                request.session['token'] = token

                back = request.COOKIES.get('back')
                if back == 'market':
                    return redirect('axf:marketbase')

                return redirect('axf:mine')
            else:
                return render(request, 'mine/login.html', context={'ps_err': '密码错误'})
        else:
            return render(request,'mine/login.html',context={'us_err':'邮箱错误'})




def logout(request):
    request.session.flush()
    return redirect('axf:mine')


def checkemail(request):
    email = request.GET.get('email')

    users = User.objects.filter(email=email)
    if users.exists():
        response_data = {
            'status': -1,
            'msg': '账号被占用'
        }
    else:
        response_data = {
            'status':1,
            'msg':'账号可以使用'
        }
    return JsonResponse(response_data)


def addcart(request):
    goodsid = request.GET.get('goodsid')
    token = request.session.get('token')
    userid = cache.get(token)

    if userid:
        user = User.objects.get(pk=userid)
        goods = Goods.objects.get(id=goodsid)
        carts = Cart.objects.filter(user=user).filter(goods=goods)
        if carts.exists():
            cart = carts.first()
            cart.number = cart.number + 1
            cart.save()
        else:
            cart = Cart()
            cart.user = user
            cart.goods = goods
            cart.number = 1
            cart.save()

        response_data = {
            'msg':'成功添加商品',
            'status':1,
            'number':cart.number
        }

    else:
        response_data = {
            'msg':'未登录',
            'status':-1
        }

    return JsonResponse(response_data)


def subcart(request):
    goodsid = request.GET.get('goodsid')
    goods = Goods.objects.get(id=goodsid)

    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    cart = Cart.objects.filter(user=user).filter(goods=goods).first()

    cart.number = cart.number - 1
    cart.save()

    response_dir = {
        'msg':'减操作成功',
        'status':1,
        'number':cart.number
    }
    return JsonResponse(response_dir)


def changecartselect(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    cart.isselect = not cart.isselect
    cart.save()

    response_data = {
        'msg':'选中状态更改成功',
        'status':1,
        'isselect':cart.isselect,
    }
    return JsonResponse(response_data)


def changecartall(request):
    isall = request.GET.get('isall')
    token = request.session.get('token')
    userid = cache.get(token)
    user = User.objects.get(pk=userid)
    carts = user.cart_set.all()

    if isall == 'true':
        isall = True
    else:
        isall = False

    for cart in carts:
        cart.isselect = isall
        cart.save()

    response_data = {
        'msg':'全选选择成功',
        'status':1,
    }

    return JsonResponse(response_data)