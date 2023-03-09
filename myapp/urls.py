from django.urls import path

from .views import DirectorsListAPIView, GenresListAPIView, FilmsListAPIView, AfishaListAPIView, DirectorsRetrieveUpdateDestroyAPIView, GenresRetrieveUpdateDestroyAPIView, FilmsRetrieveUpdateDestroyAPIView, AfishaRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('directors/', DirectorsListAPIView.as_view()),
    path('genres/', GenresListAPIView.as_view()),
    path('films/', FilmsListAPIView.as_view()),
    path('afisha/', AfishaListAPIView.as_view()),
    path('directors/<int:pk>/', DirectorsRetrieveUpdateDestroyAPIView.as_view()),
    path('genres/<int:pk>/', GenresRetrieveUpdateDestroyAPIView.as_view()),
    path('films/<int:pk>/', FilmsRetrieveUpdateDestroyAPIView.as_view()),
    path('afisha/<int:pk>/', AfishaRetrieveUpdateDestroyAPIView.as_view()),
]