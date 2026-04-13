from django.shortcuts import render
from .models import Movie, Director
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import MovieSerializer, DirectorSerializer

# Create your views here.

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    # @action(detail=True, methods=['get'])
    # def products(self, request, pk=None):



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer