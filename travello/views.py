from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.

def index(request):
    #return HttpResponse("Hello Traveller")
    """dest1 = Destination()
    dest2 = Destination()
    dest3 = Destination()
    dest1.update("Shimla", "travello/images/destination_4.jpg", "Hill Queen", 2000, False)
    dest2.update("Palampur", "travello/images/destination_2.jpg", "Tea Gardens", 1000, True)
    dest3.update("Mandi", "travello/images/destination_3.jpg", "Chotti Kashi", 1500, False)
    """
    destinations = Destination.objects.all()
    for dest in destinations:
        print("Image url is ", dest.image.url)
    return render(request, 'travello/index.html', {'destinations': destinations})