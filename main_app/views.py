from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Hamster, Toy
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
    id_list = hamster.toys.all().values_list('id')
    toys_hamster_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'hamsters/detail.html', {'hamster': hamster, 'feeding_form': feeding_form, 'toys': toys_hamster_doesnt_have})

def add_feeding(request, hamster_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.hamster_id = hamster_id
        new_feeding.save()
    return redirect('detail', hamster_id=hamster_id)

def assoc_toy(request, hamster_id, toy_id):
    # Note that you can pass a toy's id instead of the whole toy object
    Hamster.objects.get(id=hamster_id).toys.add(toy_id)
    return redirect('detail', hamster_id=hamster_id)

class HamsterCreate(CreateView):
    model = Hamster
    fields = ['name', 'color', 'description', 'age']

class HamsterUpdate(UpdateView):
    model = Hamster
    fields = ['color', 'description', 'age']

class HamsterDelete(DeleteView):
    model = Hamster
    success_url = '/hamsters'

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'