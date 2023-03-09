from django.urls import path, include
from rest_framework import routers

from .views import AnimalViewSet, CategoryViewSet, AnimalTypeViewSet, StatusViewSet, StatusOrderViewSet, OrderViewSet

router = routers.SimpleRouter()
router.register('animals', AnimalViewSet)
router.register('categories', CategoryViewSet)
router.register('animal_types', AnimalTypeViewSet)
router.register('statuses', StatusViewSet)
router.register('status_orders', StatusOrderViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
