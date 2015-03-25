from django.shortcuts import render,HttpResponse
from django.template.loader import render_to_string


def view_globe(request):
    return render(request, 'globe_base.html', { "body_header": "",
                                                "body_tag": "",
                                                "body_content": get_globe_body(),
                                                "body_footer": "",
                                                "includes_content": get_globe_includes(),
                                                "scripts_content": get_globe_scripts()
                                              })


def get_globe_body():
    return render_to_string('globe_body.html')


def get_globe_includes():
    return render_to_string('globe_includes.html')


def get_globe_scripts():
    return render_to_string('globe_scripts.html')