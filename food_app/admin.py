from django.contrib import admin
from .models import *

admin.site.register(FoodPlace)
admin.site.register(Menu)
admin.site.register(ReviewRating)
admin.site.register(UserReview)