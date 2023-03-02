from django.urls import path

from .views import ProductView, ProductDetailView, CategoryView, CategoryDetailView, ManufacturerView, ManufacturerDetailView

urlpatterns = [
    path('product-list/', ProductView.as_view(), name="product-list"),
    path('product-detail/<str:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('product-create/', ProductView.as_view(), name="product-create"),
    path('product-update/<str:pk>/', ProductDetailView.as_view(), name="product-update"),
    path('product-delete/<str:pk>/', ProductDetailView.as_view(), name="product-delete"),
    path('category-list/', CategoryView.as_view(), name="category-list"),
    path('category-detail/<str:pk>/', CategoryDetailView.as_view(), name="category-detail"),
    path('category-create/', CategoryView.as_view(), name="category-create"),
    path('category-update/<str:pk>/', CategoryDetailView.as_view(), name="category-update"),
    path('category-delete/<str:pk>/', CategoryDetailView.as_view(), name="category-delete"),
    path('manufacturer-list/', ManufacturerView.as_view(), name="manufacturer-list"),
    path('manufacturer-detail/<str:pk>/', ManufacturerDetailView.as_view(), name="manufacturer-detail"),
    path('manufacturer-create/', ManufacturerView.as_view(), name="manufacturer-create"),
    path('manufacturer-update/<str:pk>/', ManufacturerDetailView.as_view(), name="manufacturer-update"),
    path('manufacturer-delete/<str:pk>/', ManufacturerDetailView.as_view(), name="manufacturer-delete"),
]
