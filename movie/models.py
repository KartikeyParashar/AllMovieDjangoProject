from django.db import models

# Create your models here.


class Actor(models.Model):
    actor_name = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    dob = models.DateField(max_length=8, blank=True, null=True)
    bio = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.actor_name


class Producer(models.Model):
    producer_name = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    dob = models.DateField(max_length=8, blank=True, null=True)
    bio = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.producer_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    release_date = models.DateField(max_length=8, blank=True, null=True)
    plot = models.CharField(max_length=500, blank=True, null=True)
    poster = models.URLField(blank=True, null=True)
    actor = models.ManyToManyField(Actor, related_name='actor', blank=True)
    producer = models.ManyToManyField(Producer, related_name='producer', blank=True)

    def __str__(self):
        return self.movie_name
