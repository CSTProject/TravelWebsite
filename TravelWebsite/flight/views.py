from django.shortcuts import render
from .airline import OneWay,RoundTrip
# Create your views here.

def flightform(request):
    return render(request, 'flight/form.html')

def flightresultdataOneWay(request):
    origin = request.GET.get('origin')
    adults = request.GET.get('adults')
    destination = request.GET.get('dest')
    date = request.GET.get('date')
    childs = request.GET.get('childs')
    infants = request.GET.get('infants')
    Spider = OneWay()
    passthis = Spider.GetDictionary(origin,destination,date,adults,childs,infants)

    return render(request, 'flight/result_o.html', passthis)


def flightresultdataRoundTrip(request):
    origin = request.GET.get('origin')
    adults = request.GET.get('adults')
    destination = request.GET.get('dest')
    date1 = request.GET.get('date1')
    date2 = request.GET.get('date2')
    childs = request.GET.get('childs')
    infants = request.GET.get('infants')
    Spider = RoundTrip()
    data = Spider.GetDictionary(origin, destination, date1,date2, adults, childs, infants)

    return render(request, 'flight/result_r.html', data)