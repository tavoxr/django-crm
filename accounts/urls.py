from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<int:id_customer>/', views.customer, name="customer"),
    path('create_order/', views.createOrder, name="createOrder"),
    path('edit_order/<int:id_order>/', views.editOrder, name="edit_order" ),
    path('delete_order/<int:id_order>/', views.deleteOrder, name="delete_order"),
     

]