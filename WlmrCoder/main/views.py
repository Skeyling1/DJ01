from django.shortcuts import render


# Create your views here.
def index(request):
    data = {'caption':"Django"}
    return render(request, 'main/index.html', data)

def new(request):
    data = {'caption': "Django"}
    return render(request, 'main/new2.html', data)

def new3(request):
    data = {'caption': "Django"}
    return render(request, 'main/new3.html', data)

def new4(request):
    data = {'caption': "Django"}
    return render(request, 'main/new4.html', data)