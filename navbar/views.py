from django.shortcuts import render,HttpResponse

def view_navbar(request):
    return render(request,'jumbotron.html')
