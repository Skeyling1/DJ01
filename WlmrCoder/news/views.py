from django.shortcuts import render


# Create your views here.
def home(request):
    data = {'caption':"Django"}
    return render(request, 'news/news.html', data)