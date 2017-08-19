from django.conf.urls import url
from url_inherit import views

#TEMPLATE_TAGGING
app_name = 'urlapp'


urlpatterns = [
    url(r'^other/',views.other,name='other'),
]
