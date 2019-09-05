from django.shortcuts import render
from django.http.response import HttpResponse

def home(request):
    a="This is the Home page"
    return HttpResponse(a)

def contact(request):
    b="This is the contact page"
    return HttpResponse(b)

def services(request):
    c="This is the services page"
    return HttpResponse(c)

def feedback(request):
    d="This is the feedback page"
    return HttpResponse(d)