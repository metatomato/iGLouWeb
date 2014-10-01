from django.shortcuts import render,HttpResponse


# Create your views here.

def home_view(request):
	return HttpResponse("<html>Hola señor metaTomato!! Como està a la casa?</html>")
