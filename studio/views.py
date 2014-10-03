from django.shortcuts import render,HttpResponse


# Create your views here.

def view_home(request):
    return render(request,'base.html')	

