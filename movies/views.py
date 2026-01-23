from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie


# Movie list page
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {
        'movies': movies
    })


# Movie detail page (with trailer)
def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movies/movie_detail.html', {
        'movie': movie
    })


# Add movie (used only if you want admin-style add)
def add_movie(request):
    if request.method == "POST":
        Movie.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            duration=request.POST.get("duration"),
            release_date=request.POST.get("release_date"),
            trailer_url=request.POST.get("trailer_url")
        )
        return redirect('movie_list')

    return render(request, 'movies/add_movie.html')