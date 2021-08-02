from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('userLogin',views.userLogin,name='userLogin'),
    path('userRegister',views.userRegister,name='userRegister'),
    path('adminLogin',views.adminLogin,name='adminLogin'),
    path('logout',views.logout,name='logout'),
    path('main',views.main,name='main'),
    path('end',views.end,name='end'),
    path('authorize',views.authorize,name='authorize'),
    path('voteCast',views.voteCast,name='voteCast'),
    path('result',views.result,name='result'),
    path('vote',views.vote,name='vote'),
    path('conform1',views.conform1,name='conform1'),
    path('conform2',views.conform2,name='conform2'),
    path('conform3',views.conform3,name='conform3'),
]