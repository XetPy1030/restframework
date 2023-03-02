from django.urls import path

from .views import CartView, CartItemView, ProductView, CartItemList, CartList, ProductList

urlpatterns = [
    path('cart/', CartView.as_view()),
    path('cart/<int:pk>/', CartView.as_view()),
    path('cartitem/', CartItemView.as_view()),
    path('cartitem/<int:pk>/', CartItemView.as_view()),
    path('product/', ProductView.as_view()),
    path('product/<int:pk>/', ProductView.as_view()),
    path('cartitemlist/', CartItemList.as_view()),
    path('cartlist/', CartList.as_view()),
    path('productlist/', ProductList.as_view()),


]