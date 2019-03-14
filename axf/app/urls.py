from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^market/$', views.market, name='marketbase'),
    url(r'^market/(?P<childid>\d+)/(?P<sortid>\d+)/$', views.market, name='market'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^mine/$', views.mine, name='mine'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^checkemail/$',views.checkemail,name='checkemail'),
    url(r'^addcart/$',views.addcart,name='addcart'),

    url(r'^subcart/$',views.subcart,name='subcart'),

    url(r'^changecartselect/$',views.changecartselect,name='changecartselect'),

    url(r'^changecartall/$',views.changecartall,name='changecartall'),

    url(r'^genenateorder/$',views.genenateorder,name='genenateorder'),

    url(r'^orderlist/$',views.orderlist,name='orderlist'),

    url(r'^orderdetail/(?P<identifier>[\d.]+)/$',views.orderdetail,name='orderdetail'),

    url(r'^returnurl/$',views.returnurl,name='returnurl'),

    url(r'^appnotifyurl/$',views.appnotifyurl,name='appnotifyurl'),

    url(r'^pay/$',views.pay,name='pay'),

]
