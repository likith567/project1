from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hai(request):
    return HttpResponse("these is likith")

def hello(request):
    return HttpResponse("these is likith2")

def hay(request):
    return HttpResponse("<h1><marquee>These is Nani</marquee></h2>")
def liki(request):
    return HttpResponse("<h1> Iam Nani </h1>")