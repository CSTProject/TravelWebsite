from django.shortcuts import render
from .forms import FForm
from .airline import Spider
# Create your views here.

def flightresult(request, formdata):
	flight = Spider(formdata['origin'],formdata['destination'],formdata['date'],formdata['adults'],formdata['childs'],formdata['infants'])
	dictionary = flight.GetDictionary()
	print (dictionary)
	return render(request, 'flight/form.html', dictionary) 
def flightform(request):
	form = FForm(request.POST or None)
	if form.is_valid():
		formdata = form.cleaned_data
		print (formdata)
		flightresult(request,formdata)
	context = {"form":form, }
		
	return render(request, 'flight/form.html', context)

		

		