from django.urls import path
from .views import main_page, price_page, cart_page, sign_up_by_django, Menu

urlpatterns = [
    path('', main_page, name='main_page'),
    path('price/', price_page, name='price_page'),
    path('cart/', cart_page, name='cart_page'),
    path('menu/', Menu.as_view(), name='menu'),
    path('sign_up/', sign_up_by_django, name='sign_up'),
]
