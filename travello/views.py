from django.shortcuts import render
from .models import Destinations


# Create your views here.
def index(request):
    dest1 = Destinations()
    dest1.name = "Greece"
    dest1.description = "Good place to visit."
    dest1.price = "1,764"
    dest1.img = "destination_6.jpg"
    dest1.offer = True

    dest2 = Destinations()
    dest2.name = "Great Britain"
    dest2.description = "England is pretty cool."
    dest2.price = "1,335"
    dest2.img = "destination_1.jpg"
    dest2.offer = True

    dest3 = Destinations()
    dest3.name = "Dublin"
    dest3.description = "Rolling countryside by a great city."
    dest3.price = "2,100"
    dest3.img = "destination_2.jpg"
    dest3.offer = False

    dest4 = Destinations()
    dest4.name = "Cairo"
    dest4.description = "Not too far from the great pyramids!"
    dest4.price = "3,300"
    dest4.img = "destination_3.jpg"
    dest4.offer = False

    dest5 = Destinations()
    dest5.name = "Berlin"
    dest5.description = "Pretzel and beer lovers welcome!"
    dest5.price = "2,567"
    dest5.img = "destination_4.jpg"
    dest5.offer = True

    dest6 = Destinations()
    dest6.name = "Tokyo"
    dest6.description = "Amazing to visit during cherry blossom season."
    dest6.price = "4,043"
    dest6.img = "destination_5.jpg"
    dest6.offer = False

    dest = [dest1, dest2, dest3, dest4, dest5, dest6]
    return render(request, "index.html", {'dests': dest})


def news(request):
    return render(request, "news.html")


def destinations(request):
    return render(request, "destinations.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")
