from django.shortcuts import render
from .models import Hamster
# hamsters = [
  #  {'name': 'Dune', 'color': 'blonde', 'description': 'Young and full of life', 'age': 1},
   # {'name': 'Atreides', 'color': 'black', 'description': 'Quiet and gentle', 'age': 2},
    #{'name': 'Harkonnen', 'color': 'white', 'description': 'Angry. So angry.', 'age': 3},
#]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def hamsters_index(request):
    hamsters = Hamster.objects.all()
    return render(request, 'hamsters/index.html', {'hamsters': hamsters})

def hamster_detail(request, hamster_id):
    hamster = Hamster.objects.get(id=hamster_id)
    return render(request, 'hamsters/detail.html', {'hamster': hamster})