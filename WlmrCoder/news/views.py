from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm


# Create your views here.
def home(request):
    news = News_post.objects.all()
    data = {'caption': "Django", 'news': news}
    return render(request, 'news/news.html', data)

def add_news(request):
    error = ""
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Данные были заполнены не корректно"
    form = News_postForm()
    data = {'caption': "Django", 'form': form, 'error': error}
    return render(request, 'news/news_add.html', data)

