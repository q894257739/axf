import hashlib
import random

import time


from django.core.cache import cache
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow, FoodType, Goods, User


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

    return render(request,'market/market.html',context=rensponse_dir)


def cart(request):
    return render(request,'cart/cart.html')


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


def lougin(request):
    if request.method == 'GRT':
        return render()
    return None


def logout(request):
    request.session.flush()
    return redirect('axf:mine')