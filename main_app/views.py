from django.shortcuts import render
hamsters = [
    {'name': 'Dune', 'color': 'blonde', 'description': 'Young and full of life', 'age': 1},
    {'name': 'Atreides', 'color': 'black', 'description': 'Quiet and gentle', 'age': 2},
    {'name': 'Harkonnen', 'color': 'white', 'description': 'Angry. So angry.', 'age': 3},
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def hamsters_index(request):
    return render(request, 'hamsters/index.html', {'hamsters': hamsters})