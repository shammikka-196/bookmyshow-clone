from django.contrib import admin
from .models import Movie
admin.site.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'language')