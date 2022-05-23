from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from food_app.views import  SignUpView
from django.contrib.auth.views import ( LoginView, LogoutView,
                                        PasswordChangeView,
                                        )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("food_app.urls")),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "food_app.views.page_not_found_view"