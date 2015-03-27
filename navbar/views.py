from django.shortcuts import render,HttpResponse
from django.template.loader import render_to_string


def view_navbar(request):
    return render(request,'navbar.html')


def get_navbar_body(links):
    return render_to_string('navbar_body.html',{'links':links})


def get_navbar_body_tag():
    body_tag = ' data-spy= scroll  data-offset= 60  data-target= .navbar  '
    return body_tag


def get_navbar_includes():
    return render_to_string('navbar_includes.html')


def get_navbar_scripts():
    return render_to_string('navbar_scripts.html')