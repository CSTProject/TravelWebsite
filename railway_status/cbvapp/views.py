from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from . import models
from cbvapp.railway import LiveTrain


class IndexView(TemplateView):
    template_name = 'main.html'

def getData(request):

    train_no = request.GET.get('number')
    date = request.GET.get('date')
    lts = LiveTrain(train_no,date)
    list = lts.routelist()
    return render(request,'result.html',{'livestatus':list})



