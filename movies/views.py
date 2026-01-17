from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Movie


# -------------------------
# TASK 1 – Movie List Page
# -------------------------
def movie_list(request):
    genre = request.GET.get('genre')
    language = request.GET.get('language')

    movies = Movie.objects.all()

    if genre:
        movies = movies.filter(genre=genre)

    if language:
        movies = movies.filter(language=language)

    return render(request, 'movies/movie_list.html', {
        'movies': movies
    })


# -------------------------
# TASK 2 – Theater List Page
# -------------------------
def theater_list(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    theaters = [
        "PVR Cinemas",
        "INOX",
        "IMAX",
        "Cinepolis"
    ]

    return render(request, 'movies/theater_list.html', {
        'movie': movie,
        'theaters': theaters
    })


# -------------------------
# TASK 2 – Booking Success + Email
# -------------------------
def booking_success(request):
    user_email = "testuser@gmail.com"   # later replace with logged-in user
    movie_name = "Sample Movie"
    seats = "A1, A2"
    amount = "300"

    send_mail(
        subject="🎟 Ticket Booking Confirmation",
        message=f"""
Your booking is confirmed!

Movie: {movie_name}
Seats: {seats}
Amount Paid: ₹{amount}

Enjoy your movie 🍿
""",
        from_email="noreply@bookmyshowclone.com",
        recipient_list=[user_email],
        fail_silently=True,   # keeps app running even if email not configured
    )

    return render(request, 'movies/booking_success.html')