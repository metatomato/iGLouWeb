from django.shortcuts import render,HttpResponse
from django.template.loader import render_to_string
from navbar.views import view_navbar,get_navbar_body,get_navbar_body_tag,get_navbar_includes,get_navbar_scripts
from news.views import get_news_body,get_news_includes,get_news_scripts

# Create your views here.


def view_home(request):
    return render(request, 'base.html', {"body_header": view_studio_body_header(),
                                         "body_tag": get_navbar_body_tag(),
                                         "body_content": view_studio_body_content(),
                                         "body_footer": view_studio_body_footer(),
                                         "includes_content": view_studio_includes(),
                                         "scripts_content": view_studio_scripts()
                                         })


def view_studio_body_header():
    content = get_navbar_body()
    content += get_studio_body_header()
    return content

def view_studio_body_content():
    content = get_news_body()
    content += get_studio_body_content()
    return content

def view_studio_body_footer():
    content = get_studio_body_footer()
    return content

def view_studio_includes():
    content = get_navbar_includes()
    content += get_news_includes()
    content += get_studio_includes()
    return content

def view_studio_scripts():
    content = get_navbar_scripts()
    content += get_studio_body_scripts()
    #content += get_news_scripts()
    return content




def get_studio_body_content():
    content_services = render_to_string('studio_body.html')
    content_framework = render_to_string('studio_body_framework.html')
    content_about = render_to_string('studio_body_about.html')
    content = content_services + content_framework + content_about
    return content

def get_studio_body_scripts():
    content_services = render_to_string('studio_scripts.html');
    content_framework = render_to_string('studio_scripts_framework.html')
    content = content_services + content_framework

    return content

def get_studio_body_header():
    content = render_to_string('studio_body_header.html')
    return content

def get_studio_body_footer():
    content = render_to_string('studio_body_footer.html')
    return content

def get_studio_includes():
    content = render_to_string('studio_includes.html')
    return content
