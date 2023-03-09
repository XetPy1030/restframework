from rest_framework import serializers

from .models import Directors, Genres, Films, Afisha


class DirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directors
        fields = '__all__'


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = '__all__'


class AfishaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afisha
        fields = '__all__'
