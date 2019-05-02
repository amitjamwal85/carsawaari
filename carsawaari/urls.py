from django.conf.urls import  url
from carsawaari import views
urlpatterns=[
    url(r'^$', views.main, name='main'),
    url(r'^carpool$', views.carpool, name='carpool'),
    url(r'^joinpool$', views.joinpool, name='joinpool'),
    url(r'^getcity$', views.getcity, name='getcity'),
    url(r'^test$', views.test, name='test'),
]