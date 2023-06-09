from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):

    return render(request, 'index.html', {})


def about(request):
    return HttpResponse("My name is Vadim")


def contacts(request):
    return render(request, 'contacts.html', {})


def hobbies(request):
    return HttpResponse("My hobbies")



def gallery(request):
    return HttpResponse("My gallery")


def photo(request):
    return HttpResponse("My photo")

def obomne(request):
    return render(request, 'obomne.html', {})


def podrobnee(request):
    return render(request, 'podrobnee.html', {})


def echo(request):
    return render(request, 'echo.html', {})

def services(request):
    return render(request, 'services.html', {})