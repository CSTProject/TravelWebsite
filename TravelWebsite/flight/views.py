from django.shortcuts import render
from .forms import FForm
from .airline import Spider
# Create your views here.

def flightresult(request):
    form = FForm(request.GET)

    return render(request, 'flight/form.html')
def flightresultdata(request):
    origin = request.GET.get('origin')
    adults = request.GET.get('adults')
    destination = request.GET.get('dest')
    date = request.GET.get('date')
    childs = request.GET.get('childs')
    infants = request.GET.get('infants')
    flight = Spider(origin,destination,date,adults,childs,infants)
    passthis = flight.GetDictionary()
    '''
    DUMMY DATA FOR TESTING
    passthis ={'Time': ['1h 5m', '55m', '1h 5m', '1h 5m', '1h 10m', '1h', '1h 15m', '1h 15m', '1h 10m', '1h 10m', '1h 15m',
              '1h 5m', '1h 10m', '25h 50m', '17h 35m', '10h', '8h 35m', '11h 30m', '21h 15m', '6h 35m', '26h 45m',
              '9h 35m', '25h 10m', '29h 30m', '21h 20m', '26h 55m'],
     'Stops': ['non-stop', 'non-stop', 'non-stop', 'non-stop', 'non-stop', 'non-stop', 'non-stop', 'non-stop',
               'non-stop', 'non-stop', 'non-stop', 'non-stop', 'non-stop', '1 stop', '1 stop', '1 stop', '1 stop',
               '1 stop', '1 stop', '1 stop', '2 stops', '2 stops', '2 stops', '2 stops', '2 stops', '2 stops'],
     'Serial': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                '19', '20', '21', '22', '23', '24', '25'],
     'Prices': ['Rs.7,552', 'Rs.12,360', 'Rs.12,360', 'Rs.12,360', 'Rs.13,416', 'Rs.15,348', 'Rs.15,448', 'Rs.15,448',
                'Rs.15,448', 'Rs.16,076', 'Rs.16,076', 'Rs.17,968', 'Rs.19,648', 'Rs.31,064', 'Rs.31,064', 'Rs.31,064',
                'Rs.31,064', 'Rs.31,064', 'Rs.33,920', 'Rs.35,396', 'Rs.44,636', 'Rs.44,636', 'Rs.44,636', 'Rs.44,636',
                'Rs.44,636', 'Rs.46,184'],
     'Vendor': ['Air India', 'SpiceJet', 'SpiceJet', 'SpiceJet', 'IndiGo', 'Vistara', 'Jet Airways', 'Jet Airways',
                'Jet Airways', 'Jet Airways', 'Jet Airways', 'Jet Airways', 'Jet Airways', 'Jet Airways', 'Jet Airways',
                'Jet Airways', 'Jet Airways', 'Jet Airways', 'Jet Airways', 'Jet Airways', 'Jet Airways', 'Jet Airways',
                'Jet Airways', 'Jet Airways', 'Jet Airways', 'Jet Airways'],
     'DepartTime': ['12:50', '08:40', '16:10', '20:25', '12:00', '15:20', '09:35', '10:55', '21:35', '15:15', '19:40',
                    '07:35', '18:05', '11:15', '11:15', '11:15', '11:15', '11:15', '11:15', '11:15', '11:15', '11:15',
                    '11:15', '11:15', '11:15', '11:15'],
     'Route': ['IXC → DEL', 'IXC → DEL', 'IXC → DEL', 'IXC → DEL', 'IXC → DEL', 'IXC → DEL', 'IXC → DEL', 'IXC → DEL',
               'IXC → DEL', 'IXC → DEL', 'IXC → DEL', 'IXC → DEL', 'IXC → DEL', 'IXC → JAI → DEL', 'IXC → JAI → DEL',
               'IXC → JAI → DEL', 'IXC → JAI → DEL', 'IXC → JAI → DEL', 'IXC → JAI → DEL', 'IXC → JAI → DEL',
               'IXC → JAI → LKO → DEL', 'IXC → JAI → LKO → DEL', 'IXC → JAI → LKO → DEL', 'IXC → JAI → LKO → DEL',
               'IXC → JAI → LKO → DEL', 'IXC → JAI → UDR → DEL'],
     'ArrivalTime': ['13:55', '09:35', '17:15', '21:30', '13:10', '16:20', '10:50', '12:10', '22:45', '16:25', '20:55',
                     '08:40', '19:15', '13:05 01 Sep', '04:50 01 Sep', '21:15', '19:50', '22:45', '08:30 01 Sep',
                     '17:50', '14:00 01 Sep', '20:50', '12:25 01 Sep', '16:45 01 Sep', '08:35 01 Sep', '14:10 01 Sep']}'''
    return render(request, 'flight/result.html', passthis)

