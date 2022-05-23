from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CreateFoodPlace(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreateFoodPlace, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(
            username=self.request.user)

    user = forms.ModelChoiceField(queryset=None, initial=0)
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Food Place Name ?', 'class': 'form-control'}),
        label='Name')
    owner_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Owner Name ?', 'class': 'form-control'}),
                                 label='Owner Name')
    thumbnail = forms.ImageField()
    location = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Address in Text', 'class': 'form-control'}),
        label='Your Address')
    maps_location_link = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Live Location on Maps Link', 'class': 'form-control'}),
        label='Maps Live Location Link')
    description = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Your Description in 500 words ...', 'rows': 5, 'class': 'form-control'}),
        max_length=500,
        label="Message", required=True)
    zomato_link = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Zoamto Order Link', 'class': 'form-control'}),
        label='Zomato Link')

    class Meta:
        model = FoodPlace
        fields = ('user', 'name', 'owner_name', 'thumbnail', 'location', 'maps_location_link', 'description','zomato_link', )


class UpdateFoodPlace(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Food Place Name ?'}),
                           label='Name')
    owner_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Owner Name ?'}),
                                 label='Owner Name')
    thumbnail = forms.ImageField()
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Address in Text'}),
                               label='Your Address')
    maps_location_link = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Live Location on Maps Link'}),
        label='Maps Live Location Link')
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Description in 500 words ...', 'rows': 5}),
        max_length=500,
        label="Message", required=True)
    active = models.BooleanField()

    class Meta:
        model = FoodPlace
        fields = ('name', 'owner_name', 'thumbnail', 'location', 'maps_location_link', 'description','zomato_link', 'active', )


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ('rating', 'review')


class UpdateReviewForm(forms.ModelForm):
    rating = forms.FloatField()
    review = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Description in 500 words ...', 'rows': 5}),
        max_length=500,
        label="Message", required=True)

    class Meta:
        model = ReviewRating
        fields = ('rating', 'review')


class CreateUserReview(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(CreateUserReview, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(
            username=self.request.user)

    user = forms.ModelChoiceField(queryset=None, initial=0)
    food_place_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Food Place Name ?'}),
                                      label='Name')
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Address in Text'}),
                               label='Your Address')
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Live Location on Maps Link'}),
                              label='Maps Live Location Link')
    review = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Description in 500 words ...', 'rows': 5}),
        max_length=500,
        label="Message", required=True)

    class Meta:
        model = UserReview
        fields = ('user', 'food_place_name', 'location', 'subject', 'review',)


class UpdateUserReview(forms.ModelForm):
    food_place_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Food Place Name ?'}),
                                      label='Name')
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Address in Text'}),
                               label='Your Address')
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Live Location on Maps Link'}),
                              label='Maps Live Location Link')
    review = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Your Description in 500 words ...', 'rows': 5}),
        max_length=500,
        label="Message", required=True)

    class Meta:
        model = UserReview
        fields = ('food_place_name', 'location', 'subject', 'review',)
