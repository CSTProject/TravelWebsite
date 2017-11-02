from django.shortcuts import render
from .airline import OneWay,RoundTrip
# Create your views here.

def flightform(request):
    return render(request, 'flight/form.html')

def flightresultdataOneWay(request):
    origin = request.GET.get('origin')
    adults = request.GET.get('adults')
    destination = request.GET.get('dest')
    date1 = request.GET.get('date')
    date=''
    count = 0
    temp = date1.split('-')
    temp.reverse()
    for x in temp:
        if count!=0:
            date+= '/' + x
        else:
            date+= x
        count+=1

    childs = request.GET.get('childs')
    infants = request.GET.get('infants')
    Spider = OneWay()
    passthis = Spider.GetDictionary(origin,destination,date,adults,childs,infants)

    return render(request, 'flight/result_o.html', passthis)


def flightresultdataRoundTrip(request):
    origin = request.GET.get('origin')
    adults = request.GET.get('adults')
    destination = request.GET.get('dest')
    tempp = []
    tempp.append(request.GET.get('date1'))
    tempp.append(request.GET.get('date2'))

    date = []
    for date1 in tempp:
        count = 0
        temp = date1.split('-')
        temp.reverse()
        str = ''
        for x in temp:
            if count != 0:
                str += '/' + x
            else:
                str += x
            count += 1
        date.append(str)

    childs = request.GET.get('childs')
    infants = request.GET.get('infants')
    Spider = RoundTrip()
    data = Spider.GetDictionary(origin, destination, date[0],date[1], adults, childs, infants)

    return render(request, 'flight/result_r.html', data)