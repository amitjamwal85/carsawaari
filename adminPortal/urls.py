from django.conf.urls import include, url
from adminPortal import views
from django.urls import path
urlpatterns=[
    url(r'^admin.login$',views.index,name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^verfiyCar$', views.verfiyCar, name='verfiyCar'),
    url(r'^verfiyID$', views.verfiyID, name='verfiyID'),
    url(r'^Promotion$', views.Promotion, name='Promotion'),
    url(r'^SendNotification$', views.SendNotification, name='SendNotification'),
    #url(r'^admin$', views.admin, name='verfiyID'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^appDis$', views.appDis, name='appDis'),
    url(r'^CarVer$', views.CarVer, name='appDisCar'),
    url(r'^users$', views.users, name='users'),
    url(r'^tripRequest$', views.tripRequest, name='users'),
    url(r'^userinfo$', views.userinfo, name='userinfo'),
    url(r'^tripInfo$', views.tripInfo, name='tripInfo'),
    url(r'^offer$', views.offer, name='offer'),
    url(r'^groupInfo$', views.groupInfo, name='offer'),
    url(r'^groupall$', views.groupall, name='groupall'),
]