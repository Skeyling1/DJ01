from django.shortcuts import render
from .models import News_post


# Create your views here.
def home(request):
    news = News_post.objects.all()
    data = {'caption': "Django", 'news': news}
    return render(request, 'news/news.html', data)

def add_news(request):

    data = {'caption': "Django"}
    return render(request, 'news/news_add.html', data)

