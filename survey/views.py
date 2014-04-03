from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "home.html")


def billing(request):
    return render(request, "network-approvals(1).html")