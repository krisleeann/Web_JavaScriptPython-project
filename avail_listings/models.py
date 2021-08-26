from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing_owner")
    title = models.CharField(max_length=64)
    location = models.CharField(max_length=30)
    description = models.TextField()
    category = models.CharField(max_length=30)
    dates = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user}'s Listing {self.title}: {self.location} {self.category} {self.dates} {self.description} "


class Apply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applicant")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    experience = models.TextField()

    def __str__(self):
        return f"Submit application for {self.listing} with your experience: {self.experience}."


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.category}"


class Event(models.Model):
    title = models.CharField(max_length=64)
    location = models.CharField(max_length=30)
    description = models.TextField()
    date = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}: {self.location} {self.description}, {self.date}"
