from django.shortcuts import render,HttpResponse
from django.template.loader import render_to_string

def view_navbar(request):
    return render(request,'navbar.html')

def view_navbar_body():
    return render_to_string('navbar_body.html')