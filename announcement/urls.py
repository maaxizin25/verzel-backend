import os
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("announcement", views.AnnouncementCreateView.as_view()),
    path("announcement/<int:id>", views.AnnouncementDetailView.as_view()),
    path("announcement/images/<int:id>", views.ImageDeleteView.as_view())
]