from django.urls import path
from django.contrib.auth import views as auth_view


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
    path('password_reset',auth_view.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password_reset_sent',auth_view.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),name='password_reset_sent'),
    path('reset/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_done',auth_view.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),

   
    
    
    
    path('createOrder/<str:pk>',views.createOrder, name='createOrder'),
    path('updateOrder/<str:pk>',views.updateOrder, name='updateOrder'),
    path('deleteOrder/<str:pk>',views.deleteOrder, name='deleteOrder'),
    path('createCustomer/',views.createCustomer, name='createCustomer'),
]

'''
    template_name='accounts/password_reset.html'
    
    template_name='accounts/password_reset_confirm.html'
    
    
    
''',
