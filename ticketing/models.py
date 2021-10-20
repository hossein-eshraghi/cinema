from django.db import models


# Create your models here.

class Movie(models.Model):
    """
    Represents a movie
    """
    # name : in field text hast
    name = models.CharField(max_length=100)
    # director : in field text hast
    director = models.CharField(max_length=50)
    # year : in field numerical hast
    year = models.IntegerField()
    # length : in field numerical hast
    length = models.IntegerField()
    # description : in field text hast
    description = models.TextField()

    def __str__(self):
        return self.name


class Cinema(models.Model):
    """
    Represents a cinema saloon
    """
    cinema_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30, default='تهران')
    capacity = models.IntegerField()
    phone = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name
