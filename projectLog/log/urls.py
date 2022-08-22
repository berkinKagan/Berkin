from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("delete/<event_id>", views.delete, name="delete"),
    path("search/", views.search, name="search"),
    path("post/<str:pk>", views.post, name="post"),
]
