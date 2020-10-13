from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.site,name='site'),
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.loginPage,name='login'),
    path('createblog',views.createblog,name='createblog'),
    path('logout',views.logoutPage,name='logout'),
    path('myblog',views.myblog,name='myblog'),
    path('blogdetail/<int:pk>',views.blogdetail,name='blogdetail'),
    path('createcomments/<int:pk>',views.createcomments,name='createcomments'),
    path('createreply/<int:pk>',views.createreply,name='createreply'),
    path('sendreply/<int:pk>',views.sendreply,name='sendreply'),
]
