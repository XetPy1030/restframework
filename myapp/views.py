from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .models import Directors, Genres, Films, Afisha
from .serializers import DirectorsSerializer, GenresSerializer, FilmsSerializer, AfishaSerializer


class DirectorsListAPIView(ListAPIView):
    queryset = Directors.objects.all()
    serializer_class = DirectorsSerializer


class GenresListAPIView(ListAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


class FilmsListAPIView(ListAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer


class AfishaListAPIView(ListAPIView):
    queryset = Afisha.objects.all()
    serializer_class = AfishaSerializer


class DirectorsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Directors.objects.all()
    serializer_class = DirectorsSerializer


class GenresRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


class FilmsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer


class AfishaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Afisha.objects.all()
    serializer_class = AfishaSerializer


