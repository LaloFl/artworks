from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("author/<str:author_id>", views.author, name="author"),
    path("artworks/", views.search, name="search"),
    path("artworks/<int:artwork_id>", views.artwork, name="artwork"),
    path("collections/", views.collections, name="collections"),
    path(
        "add_to/<str:collection_id>/<int:artwork_id>", views.add_to, name="collections"
    ),
    path("accounts/register/", views.register, name="register"),
]
