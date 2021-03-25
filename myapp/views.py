from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#view -> view function is a python function that takes a web
#request and return a response (this response can be the HTML
#content or redirect, or a 404, doc/image)

def home(request):
    return HttpResponse("Hello, Welcome to first Django Project")


def about(request):
    return HttpResponse("this is about us page")


def contact(request):
    return HttpResponse("this Contact up view")


