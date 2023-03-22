

from django.urls import path
from app import views

urlpatterns = [
    path("",views.loginuser, name='login'),
    path("home",views.index1, name='home'),
    # path("service", views.service ,name='service'),
    path("loginuser",views.loginuser , name='loginuser'),
    # path("signup",views.signup , name='signup'),
    path("contact",views.contact , name='contact'),
    path("about",views.about, name='about'),
    path("products",views.products, name='products'),
    path("protective",views.protective, name='protective'),
    path("ecobags",views.ecobags, name='ecobags'),
    path("corrugated",views.corrugated, name='corrugated'),
    path("tissue",views.tissue, name='tissue'),
    path("mushroom",views.mushroom, name='mushroom'), 
    path("carbon",views.carbon, name='carbon'),
    path("success",views.success, name='success'),
    path("contribute",views.contribute, name='contribute'),  
    path("suggest",views.suggest, name='suggest'),
]
