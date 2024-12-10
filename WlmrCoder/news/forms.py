from .models import News_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'pub_date', 'author']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'})

        }