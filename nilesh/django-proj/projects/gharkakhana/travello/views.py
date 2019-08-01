from django.shortcuts import render
from .models import Destination
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello World</h1>")
    # dest1 = Destination()
    # dest2 = Destination()
    # dest3 = Destination()
    #
    # dest1.name = "Mumbai"
    # dest1.desc = "City runs on clock"
    # dest1.price = 700
    # dest1.img = "destination_1.jpg"
    # dest1.offer=True
    #
    # dest2.name = "Bhusawal"
    # dest2.desc = "City of Banana"
    # dest2.price = 800
    # dest2.img = "destination_2.jpg"
    #
    # dest3.name = "Banaglore"
    # dest3.desc = "City of gardens"
    # dest3.price = 750
    # dest3.img = "destination_3.jpg"
    # dests=[dest1,dest2,dest3]

    dests = Destination.objects.all()
    return render(request,'index.html', {'dests': dests})
    # return render(request,'index.html')

