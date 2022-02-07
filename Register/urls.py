from django.urls import path, re_path
from django.conf.urls import include

#Importacion de vistas
from Register.views import RegisterAPI

urlpatterns = [
    re_path(r'^user/$', RegisterAPI.as_view()),
]