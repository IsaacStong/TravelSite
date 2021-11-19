from django.shortcuts import render
from .models import Destinations


# Create your views here.
def index(request):
    dest1 = Destinations()
    dest1.name = "Greece"
    dest1.description = "Good place to visit."
    dest1.price = "1,764"
    dest1.img = "destination_6.jpg"
    return render(request, "index.html", {'dest1': dest1})


def news(request):
    return render(request, "news.html")


def destinations(request):
    return render(request, "destinations.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")
