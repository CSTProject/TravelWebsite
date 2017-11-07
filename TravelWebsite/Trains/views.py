from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from . import models
from Trains.railway import LiveTrain,TrainBetweenStations


class IndexView(TemplateView):
    template_name = 'trains/main.html'

def getData(request):
    src_code = request.GET.get('sstn')
    dest_code = request.GET.get('dstn')
    date1 = request.GET.get('date')
    date = ''
    count = 0
    temp = date1.split('-')
    temp.reverse()
    for x in temp:
        if count != 0:
            date += '-' + x
        else:
            date += x
        count += 1
    print (date)
    try:
        tbs = TrainBetweenStations(src_code, dest_code, date)
        trn_list = tbs.train_btw_stations()
        print(trn_list)
    except:
        trn_list = []
        print('Cant fetch data')
    return render(request,'trains/result.html',{'trn_info':trn_list})



