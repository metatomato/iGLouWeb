from django.shortcuts import render

# Create your views here.
def view_news(request):
    return render(request,'news.html')