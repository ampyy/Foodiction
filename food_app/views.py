from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from .models import *
from .forms import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .helper_functions import *
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required


def home(request):
    foodplaces = FoodPlace.objects.filter(active=True)
    user_reviews = UserReview.objects.all()
    context = {
        'foodplaces': foodplaces,
        'user_reviews': user_reviews
    }
    return render(request, "index.html", context)


def page_not_found_view(request, exception):
    return render(request, 'page_not_found_view.html', status=404)


@login_required
def myprofile(request, slug):
    user_reviews = UserReview.objects.filter(user=request.user)
    foodplaces = FoodPlace.objects.filter(user=request.user)
    print(user_reviews)
    context = {
        'user_reviews': user_reviews,
        'foodplaces' : foodplaces

    }
    return render(request, "myprofile.html", context)


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super(SignUpView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('login')


class FoodPlaceCreateView(LoginRequiredMixin, generic.CreateView):
    model = FoodPlace
    form_class = CreateFoodPlace
    template_name = 'foodplace/add_foodplace.html'

    def get_success_url(self):
        return reverse('home')

    def get_form_kwargs(self):
        kwargs = super(FoodPlaceCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


def foodplace_detail(request, slug):
    ratings = ReviewRating.objects.filter(food_place=slug)
    avg = []
    for x in ratings:
        avg.append(x.rating)
    ans = calc(avg)
    foodplace = FoodPlace.objects.get(foodplace_uuid=slug)
    foodplace.rating = ans
    foodplace.save()
    review = False
    try:
        review_check = ReviewRating.objects.get(user=request.user, food_place=slug)
        review = True
        context = {
            'foodplace': foodplace,
            'review': review,
            'ratings': ratings,
            'ans': ans,
        }
        return render(request, "foodplace/details_foodplace.html", context)
    except:
        if request.method == 'POST':
            if request.POST.get('rating') and request.POST.get('review'):
                review = ReviewRating()
                review.user = request.user
                review.food_place = slug
                review.rating = request.POST.get('rating')
                review.review = request.POST.get('review')
                if int(review.rating) > 10:
                    review.rating = 10
                elif int(review.rating) < 0:
                    review.rating = 0
                review.save()
                ratings = ReviewRating.objects.filter(food_place=slug)
                avg = []
                for x in ratings:
                    avg.append(x.rating)
                ans = calc(avg)
                foodplace = FoodPlace.objects.get(foodplace_uuid=slug)
                foodplace.rating = ans
                foodplace.save()
                return redirect('details-foodplace', slug=slug)
        else:
            total_reviews = ReviewRating.objects.all().count()
            all_reviews = ReviewRating.objects.all()
            ans = int(ans)
            ans_list = []
            for i in range(ans):
                ans_list.append(i)
            context = {
                'foodplace': foodplace,
                'review': review,
                'ratings': ratings,
                'ans': ans,
                'ans_list' : ans_list,
                'all_reviews': all_reviews
            }

            return render(request, "foodplace/details_foodplace.html", context)


def update_food(request, slug):
    context = {}
    obj = get_object_or_404(FoodPlace, foodplace_uuid=slug)
    form = UpdateFoodPlace(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('home')
    context["form"] = form
    context["foodplace_user"] = obj.user
    return render(request, 'foodplace/update_foodplace.html', context)


def update_review(request, slug):
    context = {}
    obj = get_object_or_404(ReviewRating, food_place=slug, user=request.user)
    form = UpdateReviewForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('details-foodplace', slug=slug)
    context["form"] = form
    return render(request, 'review/update_review.html', context)


class UserReviewCreateView(LoginRequiredMixin, generic.CreateView):
    model = UserReview
    form_class = CreateUserReview
    template_name = 'review/user_review.html'

    def get_success_url(self):
        return reverse('home')

    def get_form_kwargs(self):
        kwargs = super(UserReviewCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class UserReviewUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = UserReview
    form_class = UpdateUserReview
    template_name = 'review/update_user_review.html'

    def get_success_url(self):
        return reverse('home')


class UserReviewDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = UserReview
    template_name = "review/delete_user_review.html"
    success_url = '/../../'


def search(request):
    queryset = FoodPlace.objects.all()
    queryset2 = UserReview.objects.all()
    query = request.GET.get('q')

    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query)
        ).distinct()

        queryset2 = queryset2.filter(
            Q(food_place_name__icontains=query) |
            Q(subject__icontains=query) |
            Q(location__icontains=query) |
            Q(review__icontains=query)
        ).distinct()

    context = {
        'queryset': queryset,
        'queryset2': queryset2,

    }
    return render(request, "search.html", context)
