from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.home, name='home'),
    path("add-foodplace", views.FoodPlaceCreateView.as_view(), name='add-foodplace'),
    path("details-foodplace/<str:slug>", views.foodplace_detail, name='details-foodplace'),
    path("update-foodplace/<str:slug>", views.update_food, name='update-foodplace'),
    path("update-review/<str:slug>", views.update_review, name='update-review'),
    path("add-review", views.UserReviewCreateView.as_view(), name='add-review'),
    path("update-user-review/<int:pk>", views.UserReviewUpdateView.as_view(), name='update-user-review'),
    path("delete-user-review/<int:pk>", views.UserReviewDeleteView.as_view(), name='delete-user-review'),
    path("myprofile/<str:slug>/dashboard", views.myprofile, name='myprofile'),
    path("search", views.search, name='search'),

]
