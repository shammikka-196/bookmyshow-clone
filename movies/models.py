from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    duration = models.IntegerField()
    release_date = models.DateField()
    trailer_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title