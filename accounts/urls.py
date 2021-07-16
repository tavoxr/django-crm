from re import template
from django.urls import path
from .viewsets import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', registerPage, name="register"),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    
    path('', home, name="home"),
    path('user/', userPage, name='user_page'),
    path('profile/', profile, name="profile"),
    path('products/', products, name="products"),
    path('customer/<int:id_customer>/', customer, name="customer"),

    path('create_order/<int:id_customer>/', createOrder, name="create_order"),
    path('edit_order/<int:id_order>/', editOrder, name="edit_order" ),
    path('delete_order/<int:id_order>/', deleteOrder, name="delete_order"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name = "accounts/components/reset_password.html"), 
         name="password_reset"
         
         ),
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name= "accounts/components/reset_password_sent.html"), 
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/forms/password_reset_form.html"), 
         name="password_reset_confirm"),
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view( template_name= "accounts/components/reset_password_complete.html"), 
         name="password_reset_complete"),


     

]