from django.urls import path

from . import views

urlpatterns = [
    path('drawer', views.drawer, name= 'drawer'),
    path('hello', views.hello, name= 'hello'),
    path('', views.index, name='index')
    
    
]