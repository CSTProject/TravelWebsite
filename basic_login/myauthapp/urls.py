from django.conf.urls import url
from myauthapp import views

app_name = 'myauthapp'

urlpatterns = [

    url(r'^register/',views.register,name='register'),
    url(r'^user_login/',views.user_login,name='user_login'),

]
