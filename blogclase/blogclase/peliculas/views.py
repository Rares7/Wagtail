from django.shortcuts import render
from django.views import generic
from peliculas.models import Coche
# Create your views here.

#vista de un coche
class CocheDetailView(generic.DetailView):
    model = Coche
