from django.shortcuts import render

# Create your views here.
def view_news(request):
    return render(request,'news.html')

def view_navbar_dummy(request):
    return render(request,'dummy')