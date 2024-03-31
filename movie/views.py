from django.shortcuts import render
from .models import Movie


def home(request):
    searchTerm = request.GET.get('searchMovie') #getting the input value
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})

def about(request):
    return render(request, 'about.html')