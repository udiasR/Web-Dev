from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_year = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(11.0)],)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} year:{self.release_year}"
