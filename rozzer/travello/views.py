from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
 
    dest1 = Destination()
    dest2 = Destination()
    dest3 = Destination()
    dest1.name = 'Mumbai'
    dest1.img = 'destination_1.jpg'
    dest1.desc = 'The city that never sleeps'
    dest1.price = '800'

    dest2.name = 'Delhi'
    dest2.img = 'destination_2.jpg'
    dest2.desc = 'The city that have no times'
    dest2.price = '600'

    dest3.name = 'Bangalure'
    dest3.img = 'destination_3.jpg'
    dest3.desc = 'The city to enjoy!!!!!'
    dest3.price = '900'
    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests' : dests})