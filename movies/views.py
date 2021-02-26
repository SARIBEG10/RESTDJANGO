from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata
# Create your views here.


class MovieView(viewsets.ModelViewSet):

    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer


class ActionMovieView(viewsets.ModelViewSet):

    queryset = Moviedata.objects.filter(typ='action')
    serializer_class = MovieSerializer


class ComedyMovieView(viewsets.ModelViewSet):

    queryset = Moviedata.objects.filter(typ='comedy')
    serializer_class = MovieSerializer