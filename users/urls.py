from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views


urlpatterns = [
    path("users", views.UserCreateView.as_view()),
    path("users/<int:id>", views.UserDetailView.as_view()),
    path("users/login", jwt_views.TokenObtainPairView.as_view())
]