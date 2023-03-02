from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ManufacturerSerializer, ProductSerializer, CategorySerializer
from .models import Manufacturer, Product, Category


class ProductView(APIView):
    def get(self, request: WSGIRequest):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request: WSGIRequest):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request: WSGIRequest, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    def put(self, request: WSGIRequest, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request: WSGIRequest, pk):
        product = self.get_object(pk)
        product.delete()
        return Response('Item successfully deleted!')


class ManufacturerView(APIView):
    def get(self, request: WSGIRequest):
        manufacturers = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response(serializer.data)

    def post(self, request: WSGIRequest):
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        return Response(serializer.data)


class ManufacturerDetailView(APIView):
    def get_object(self, pk):
        try:
            return Manufacturer.objects.get(id=pk)
        except Manufacturer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request: WSGIRequest, pk):
        manufacturer = self.get_object(pk)
        serializer = ManufacturerSerializer(manufacturer, many=False)
        return Response(serializer.data)

    def put(self, request: WSGIRequest, pk):
        manufacturer = self.get_object(pk)
        serializer = ManufacturerSerializer(instance=manufacturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request: WSGIRequest, pk):
        manufacturer = self.get_object(pk)
        manufacturer.delete()
        return Response('Item successfully deleted!')


class CategoryView(APIView):
    def get(self, request: WSGIRequest):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request: WSGIRequest):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class CategoryDetailView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(id=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request: WSGIRequest, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)

    def put(self, request: WSGIRequest, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request: WSGIRequest, pk):
        category = self.get_object(pk)
        category.delete()
        return Response('Item successfully deleted!')
