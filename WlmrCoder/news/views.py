from django.shortcuts import render
from .models import News_post
from .forms import News_postForm


# Create your views here.
def home(request):
    news = News_post.objects.all()
    data = {'caption': "Django", 'news': news}
    return render(request, 'news/news.html', data)

def add_news(request):
    form = News_postForm()
    data = {'caption': "Django", 'form': form}
    return render(request, 'news/news_add.html', data)

