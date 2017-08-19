from django.shortcuts import render

# Create your views here.

def flightform(request):
	return render(request, 'flight/form.html')