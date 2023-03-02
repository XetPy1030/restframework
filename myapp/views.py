from django.core.handlers.wsgi import WSGIRequest
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BookSerializer
from .models import Book


@api_view(["GET"])
def books(request):
    serializer = BookSerializer(Book.objects.all(), many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_book(request: WSGIRequest):
    serializer = BookSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["PUT"])
def edit_book(request: WSGIRequest, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookSerializer(instance=book, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_book(request: WSGIRequest, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return Response({"message": "Book deleted."})