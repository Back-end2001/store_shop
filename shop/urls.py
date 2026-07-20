from django.urls import path

import shop
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('product/<int:product_id>', product_detail, name='product'),
    path("cart/", cart, name="cart"),
    path("add-to-cart/<int:pk>/", add_to_cart, name="add_to_cart"),

    path("increase/<int:pk>/",
         increase_quantity,
         name="increase_quantity"),

    path("decrease/<int:pk>/",
         decrease_quantity,
         name="decrease_quantity"),

    path("remove/<int:pk>/",
         remove_from_cart,
         name="remove_from_cart"),

    path('checkout/', checkout, name='checkout'),

path("payment-success/", payment_success, name="payment_success"),

]
