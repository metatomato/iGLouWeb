from django.shortcuts import render
from django.template.loader import render_to_string


# Create your views here.
def view_news(request):
    return render(request, 'news.html')


def get_news_body():
    return render_to_string('news_body.html')
    #return render_to_string('dummy.html')


def get_news_body_tag():
    body_tag = ""
    return body_tag


def get_news_includes():
    return render_to_string('news_includes.html')


def get_news_scripts():
    return render_to_string('news_scripts.html')