from rest_framework import viewsets

from .models import Animal, Category, AnimalType, Status, Order, StatusOrder
from .serializers import AnimalSerializer, CategorySerializer, AnimalTypeSerializer, StatusSerializer, \
    StatusOrderSerializer, OrderSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AnimalTypeViewSet(viewsets.ModelViewSet):
    queryset = AnimalType.objects.all()
    serializer_class = AnimalTypeSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusOrderViewSet(viewsets.ModelViewSet):
    queryset = StatusOrder.objects.all()
    serializer_class = StatusOrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
