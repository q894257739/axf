from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow, FoodType, Goods


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
    return render(request,'mine/mine.html')