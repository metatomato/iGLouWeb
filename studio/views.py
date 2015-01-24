from django.shortcuts import render,HttpResponse
from django.template.loader import render_to_string
from navbar.views import view_navbar,view_navbar_body

# Create your views here.

def view_home(request):
    return render(request,'base.html',{"body_content" : view_studio_body()})


def view_studio_body():
    content = render_to_string('body.html')
    content+=view_navbar_body()
    return content