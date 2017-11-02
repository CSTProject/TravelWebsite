from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'index/home.html')

def bus(request):
	return render(request, 'index/bus.html')

def hotel(request):
	return render(request, 'index/hotel.html')

def support(request):
	return render(request, 'index/support.html')

