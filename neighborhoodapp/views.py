from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from neighborhoodapp.models import Business, Post, Profile, Neighbourhood
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'index.html', {"neighbourhoods": neighbourhoods})