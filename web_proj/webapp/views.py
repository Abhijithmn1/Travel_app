from django.shortcuts import render
from .models import Place, Team


# from .models import team


# Create your views here.
def index(request):
    obj1 = Place.objects.all()
    obj2 = Team.objects.all()

    return render(request, 'index.html', {'result': obj1, 'team': obj2})
