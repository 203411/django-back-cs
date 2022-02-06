from django.urls import path, re_path
from django.conf.urls import include

#Importacion de vistas
from loadImage.views import LoadImageTable,LoadImageTableDetail

urlpatterns = [
    re_path(r'^form/$', LoadImageTable.as_view()),
    re_path(r'^form/(?P<pk>\d+)$', LoadImageTableDetail.as_view()),    
]