from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('userLogin',views.userLogin,name='userLogin'),
    path('userRegister',views.userRegister,name='userRegister'),
    path('adminLogin',views.adminLogin,name='adminLogin'),
]