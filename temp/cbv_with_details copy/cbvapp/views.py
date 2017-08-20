from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
from . import models
from cbvapp.railway import LiveTrain

class CBView(View):
    def get(self,request):
        return HttpResponse("Hi this si from class cbv")

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ltr = LiveTrain(12616,'20-08-2017')
        ls = ltr.routelist()
        context['livestatus'] = ls
        context['injectme'] = 'BASIC INJECTION from views'
        return context

class SchoolListView(ListView):
    model = models.School



