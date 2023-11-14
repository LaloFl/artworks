from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Artwork, Collection


def register(request):
    if request.method == "POST":
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            username = f.cleaned_data.get("username")
            raw_password = f.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return HttpResponseRedirect("/")

    else:
        f = UserCreationForm()

    return render(request, "registration/registration_form.html", {"form": f})


def index(request):
    artworks = Artwork.objects.all()
    print(artworks[0].id)

    return render(request, "collection/index.html", {"data": artworks})


@csrf_exempt
def add_to(request, collection_id, artwork_id):
    if request.method == "POST":
        collection = Collection.objects.filter(name=collection_id, user=request.user)
        if len(collection) == 0:
            new_collection = Collection(name=collection_id, user=request.user)
            new_collection.save()
            collection = Collection.objects.filter(
                name=collection_id, user=request.user
            )

        artwork = Artwork.objects.get(id=artwork_id)
        collection[0].artworks.add(artwork)
        collection[0].save()
        return HttpResponse("Added to collection")


def collections(request):
    collections = Collection.objects.filter(user=request.user)
    return render(request, "collection/collections.html", {"collections": collections})


def author(request, author_id):
    artworks = Artwork.objects.filter(author__slug=author_id)
    print(len(artworks))
    return render(request, "collection/author.html", {"artworks": artworks})


def artwork(request, artwork_id):
    artwork = Artwork.objects.get(id=artwork_id)
    return render(request, "collection/artwork.html", {"artwork": artwork})


def search(request):
    if request.method == "POST":
        query = request.POST.get("query")
        artworks = Artwork.objects.filter(title__icontains=query)
        return render(request, "collection/search.html", {"data": artworks})
    else:
        return render(request, "collection/search.html")
