from django.urls import path

from .views import books, edit_book, delete_book, create_book, book

urlpatterns = [
    path("books/", books, name="books"),
    path("books/<int:pk>/", book, name="book"),
    path("books/create/", create_book, name="create_book"),
    path("books/edit/<int:pk>/", edit_book, name="edit_book"),
    path("books/delete/<int:pk>/", delete_book, name="delete_book"),
]
