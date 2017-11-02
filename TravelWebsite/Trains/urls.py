from django.conf.urls import url
from Trains import views

app_name = 'Trains'

urlpatterns = [
url(r'^$', views.IndexView.as_view()),
    url(r'^data/', views.getData,name='data'),

]
