from django.urls import path 
from django.conf.urls import url

from . import views

urlpatterns = [
    path('drawer', views.drawer, name= 'drawer'),
    path('hello', views.hello, name= 'hello'),
    path('', views.index, name='index'),
    url('submit', views.submit , name='submit')
    
]