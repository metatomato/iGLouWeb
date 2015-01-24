from django.shortcuts import render,HttpResponse
from navbar.views import view_navbar

# Create your views here.

def view_home(request):
    return view_navbar(request)
    #return render(request,'base.html')

