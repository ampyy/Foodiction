from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

class FoodPlace(models.Model):
    user = models.CharField(max_length=150)
    foodplace_uuid = models.UUIDField(default=uuid.uuid4, help_text="UNIQUE ID FOR THE BATCH",
                                editable=False)
    name = models.CharField(max_length=150)
    owner_name = models.CharField(max_length=150)
    thumbnail = models.ImageField(upload_to="files/thumbnail")
    location = models.CharField(max_length=500)
    maps_location_link = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    rating = models.FloatField(default=1)
    active = models.BooleanField(default=True)
    spam = models.BooleanField(default=False)
    zomato_link = models.CharField(max_length=500)


class Menu(models.Model):
    name = models.CharField(max_length=150)
    thumbnail = models.ImageField(upload_to="files/thumbnail")
    price = models.IntegerField(default=0)
    special = models.BooleanField(default=False)
    food_place = models.ForeignKey(FoodPlace, on_delete=models.CASCADE)


class ReviewRating(models.Model):
    user = models.CharField(max_length=150)
    food_place = models.CharField(max_length=150)
    review = models.TextField(max_length=500)
    rating = models.FloatField(validators= [MinValueValidator(0.0), MaxValueValidator(10.0)])
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user + " " + self.food_place


class UserReview(models.Model):
    user = models.CharField(max_length=150)
    food_place_name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    review = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)