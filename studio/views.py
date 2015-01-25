from django.shortcuts import render,HttpResponse
from django.template.loader import render_to_string
from navbar.views import view_navbar,get_navbar_body,get_navbar_body_tag,get_navbar_includes,get_navbar_scripts
from news.views import get_news_body,get_news_includes,get_news_scripts

# Create your views here.


def view_home(request):
    return render(request, 'base.html', {"body_header": view_studio_body_header(),
                                         "body_tag": get_navbar_body_tag(),
                                         "body_content": view_studio_body_content(),
                                         "includes_content": view_studio_includes(),
                                         "scripts_content": view_studio_scripts()
                                         })


def view_studio_body_header():
    content = get_navbar_body()
    return content


def view_studio_body_content():
    content = get_news_body()
    return content


def view_studio_includes():
    content = get_navbar_includes()
    content += get_news_includes()
    return content

def view_studio_scripts():
    content = get_navbar_scripts()
    content += get_news_scripts()
    return content