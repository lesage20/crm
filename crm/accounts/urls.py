from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('products', views.products, name='products'),
    path('customer/<str:pk>',views.customer, name='customer'),
    path('register',views.registerUser, name='register'),
    path('login',views.loginUser, name='login'),
    path('logout',views.logoutUser, name='logout'),
    path('user',views.userPage, name='user'),
    path('user-settings',views.Usettings, name='user-settings'),

    
    
    
    path('createOrder/<str:pk>',views.createOrder, name='createOrder'),
    path('updateOrder/<str:pk>',views.updateOrder, name='updateOrder'),
    path('deleteOrder/<str:pk>',views.deleteOrder, name='deleteOrder'),
    path('createCustomer/',views.createCustomer, name='createCustomer'),
]
