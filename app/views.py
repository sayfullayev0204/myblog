from django.shortcuts import render


def index(request):
    return render(request, 'home.html')

def code(request):
    return render(request, 'code.html')
