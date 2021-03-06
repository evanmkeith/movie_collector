from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENRE_CHOICES = (
    ("sci-fi", "sci-fi"), 
    ("adventure", "adventure"), 
    ("comedy", "comedy"), 
    ("romance", "romance"), 
    ("drama", "drama"), 
    ("documentary", "documentary")
)

class Movie_Props(models.Model):
    name = models.CharField(max_length=100)
    use = models.CharField(max_length=260)

    def __str__(self): 
        return self.name

class Movie(models.Model):
    
    img = models.CharField(max_length=250)
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=15, choices = GENRE_CHOICES)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movieprops = models.ManyToManyField(Movie_Props)

    def __str__(self): 
        return self.title
    
    class Meta: 
        ordering = ['year']
