from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"name": "Georgi"}
    return render(request, 'index.html', context)

def contact_page(request):
    return HttpResponse("Contact us at []")