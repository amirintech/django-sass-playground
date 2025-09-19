from django.shortcuts import render
from django.http import HttpResponse
from visits.models import PageVisit

def home_view(request):
    PageVisit.objects.create(path=request.path)
    num_visits = PageVisit.objects.filter(path=request.path).count()
    return render(request, "home.html", {"num_visits": num_visits})

def about_view(request):
    PageVisit.objects.create(path=request.path)
    num_visits = PageVisit.objects.filter(path=request.path).count()
    return render(request, "about.html", {"num_visits": num_visits})