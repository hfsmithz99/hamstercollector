from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hamster
from .forms import FeedingForm
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
    feeding_form = FeedingForm()
    return render(request, 'hamsters/detail.html', {'hamster': hamster, 'feeding_form': feeding_form})

def add_feeding(request, hamster_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.hamster_id = hamster_id
        new_feeding.save()
    return redirect('detail', hamster_id=hamster_id)

class HamsterCreate(CreateView):
    model = Hamster
    fields = '__all__'

class HamsterUpdate(UpdateView):
    model = Hamster
    fields = ['color', 'description', 'age']

class HamsterDelete(DeleteView):
    model = Hamster
    success_url = '/hamsters'