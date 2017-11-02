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
    date = request.GET.get('date')
    tbs = TrainBetweenStations(src_code,dest_code,date)
    trn_list = tbs.train_btw_stations()
    return render(request,'trains/result.html',{'trn_info':trn_list})



