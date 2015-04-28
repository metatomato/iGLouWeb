from django.shortcuts import render, HttpResponse
from django.template.loader import render_to_string
from navbar.views import view_navbar, get_navbar_body, get_navbar_body_tag, get_navbar_includes, get_navbar_scripts
from news.views import get_news_body, get_news_includes, get_news_scripts
from globe.views import get_globe_body, get_globe_scripts, get_globe_includes
from studio.studio_request import get_script_request

# Create your views here.


def view_home(request):
    return render(request, 'base.html', {"body_header": view_studio_body_header(),
                                         "body_tag": get_navbar_body_tag(),
                                         "body_content": view_studio_body_content(),
                                         "body_footer": view_studio_body_footer(),
                                         "includes_content": view_studio_includes(),
                                         "scripts_content": view_studio_scripts(request)
                                        })


def view_inners(request, request_inner):
    return render(request, 'base.html', {"body_header": view_studio_body_header(),
                                         "body_tag": get_navbar_body_tag(),
                                         "body_content": view_studio_body_content(),
                                         "body_footer": view_studio_body_footer(),
                                         "includes_content": view_studio_includes(),
                                         "scripts_content": view_studio_inners(request_inner)
                                        })

def view_globe(request):
    return render(request, 'base.html', {"body_header": view_globe_body_header(),
                                         "body_tag": get_navbar_body_tag(),
                                         "body_content": view_globe_body_content(),
                                         "body_footer": view_globe_body_footer(),
                                         "includes_content": view_globe_includes(),
                                         "scripts_content": view_globe_scripts()
                                        })


# STUDIO PAGE
# -----------------------------------------/

def view_studio_body_header():
    links = ['studio',
             'services',
             'framework',
             'about',
             'contact']
    contact = '#contact'
    content = get_navbar_body(links, contact)
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


def view_studio_scripts(request):
    content = get_navbar_scripts()
    content += get_studio_body_scripts()
    if request.method == 'GET':
        if 'request' in request.GET:
            print(get_script_request(request.GET['request']))
            content += get_script_request(request.GET['request'])
    content += get_news_scripts()

    return content

def view_studio_inners(request_tag):
    print('inner requested ' + request_tag)
    content = get_navbar_scripts()
    content += get_studio_body_scripts()
    content += get_script_request(request_tag)
    content += get_news_scripts()

    return content


# GLOBE PAGE
# -----------------------------------------/

def view_globe_body_header():
    links = ['globe',
             'sms',
             'purpose',
             'countries',
             'arcade',
             'discover',
             'preview']
    contact = '/mail'
    content = get_navbar_body(links, contact)
    content += get_studio_body_header()
    return content


def view_globe_body_content():
    content = get_globe_body()
    return content


def view_globe_body_footer():
    return view_studio_body_footer()


def view_globe_includes():
    content = get_navbar_includes()
    content += get_studio_includes()
    content += get_globe_includes()
    return content


def view_globe_scripts():
    content = get_navbar_scripts()
    content += get_studio_scripts()
    content += get_globe_scripts()
    return content



# STUDIO INNERS
# -----------------------------------------/

def get_studio_body_content():
    content_services = render_to_string('studio_body.html')
    content_framework = render_to_string('studio_body_framework.html')
    content_about = render_to_string('studio_body_about.html')
    content_contact = render_to_string('studio_body_contact.html')
    content_legals = render_to_string('studio_body_legals.html')
    content = content_services + content_framework + content_about + content_contact + content_legals
    return content


def get_studio_scripts():
    content = render_to_string('studio_scripts.html')
    return content


def get_studio_body_scripts():
    content_services = render_to_string('studio_scripts.html')
    content_framework = render_to_string('studio_scripts_framework.html')
    content_parallax = render_to_string('studio_scripts_parallax.html')
    content_maps = render_to_string('studio_scripts_maps.html')
    content = content_services + content_framework + content_parallax + content_maps

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
