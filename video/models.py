from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class VideoModel(models.Model):
    title = models.CharField(max_length=100, unique=True)
    director = models.CharField(max_length=50)
    rating = models.PositiveSmallIntegerField(validators = [MaxValueValidator(5)])
    release_date = models.DateField()
    details = models.TextField()

    def __str__(self):
        return self.title