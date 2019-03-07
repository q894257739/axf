from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow, FoodType

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


def market(request):
    try:
        foodtypes = cache.get('foodtypes')
        if foodtypes == None:
            raise Exception
    except:
        foodtypes = FoodType.objects.all()
        cache.set('foodtypes',foodtypes,60*60*24)
        foodtypes = cache.get('foodtypes')


    rensponse_dir = {
        'foodtypes':foodtypes,
    }

    return render(request,'market/market.html',context=rensponse_dir)


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')