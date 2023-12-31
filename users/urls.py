from django.urls import path

from . import views


urlpatterns = [
    path("users/", views.UserCreateView.as_view()),
    path("users/<int:id>/", views.UserDetailView.as_view())
]