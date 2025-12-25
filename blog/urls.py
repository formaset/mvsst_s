from django.urls import path
from .views import BlogIndexView, BlogDetailView

urlpatterns = [
    path("", BlogIndexView.as_view(), name="index"),
    path("<slug:slug>/", BlogDetailView.as_view(), name="detail"),
]
