from django.urls import path
from .viewsets import *

urlpatterns = [
    path('register/', registerPage, name="register"),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    
    path('', home, name="home"),
    path('user/', userPage, name='user_page'),
    path('products/', products, name="products"),
    path('customer/<int:id_customer>/', customer, name="customer"),

    path('create_order/<int:id_customer>/', createOrder, name="create_order"),
    path('edit_order/<int:id_order>/', editOrder, name="edit_order" ),
    path('delete_order/<int:id_order>/', deleteOrder, name="delete_order"),

     

]