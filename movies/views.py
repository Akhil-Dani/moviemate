from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movies


def movies(request):
    movies = Movies.objects.all()
    return render(request ,'index.html' ,{'movies' : movies})

def detail(request,id):
    movie = get_object_or_404(Movies, pk=id)
    return render(request, 'detail.html', {'movie' : movie})
    
# Create your views here.
