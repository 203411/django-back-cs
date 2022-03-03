# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os
import datetime
#Importaciones de modelos
from Profile.models import Profile
from django.contrib.auth.models import User


#IMportacion de serializers
from Profile.serializers import ProfileSerializer

class ProfileTable(APIView):

    def get_objectUser(self, idUser):
        try:
            return User.objects.get(pk = idUser)
        except User.DoesNotExist:
            return 404
    
        
    def post(self, request):
        if 'url_img' not in request.data:
            raise exceptions.ParseError(
                "No has seleccionado el archivo a subir")
        archivos = request.data['url_img']
        idUser = request.data['id_user']
        user = self.get_objectUser(idUser)
        if(user != 404):
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                profile = Profile(**validated_data)
                profile.save()
                serializer_response = ProfileSerializer(profile)
                return Response(serializer_response.data, status=status.HTTP_201_CREATED)
            return Response("Metodo post no permitido", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("User doesn't")
    
class ProfileTableDetail(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(id_user = pk)
        except Profile.DoesNotExist:
            return 404
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            idResponse = ProfileSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        archivos = request.data['url_img']
        idResponse = self.get_object(pk)
        if(idResponse != 404):
            serializer = ProfileSerializer(idResponse)
            try:
                os.remove('assets/'+str(idResponse.url_img))
            except os.error:
                print("La imagen no existe")
            idResponse.url_img = archivos
            idResponse.save()
            return Response("Todo salio bien UwU", status=status.HTTP_201_CREATED)
        else:
            return Response("No salio bien")
    
    def delete(self, request, pk):
        # idUser = request.data['id_user']
        profile = self.get_object(pk)
        if profile != 404:
            profile.url_img.delete(save=True)
            # profile.delete(save=True)
            return Response("Imagen eliminada",status=status.HTTP_204_NO_CONTENT)
        return Response("Imagen no encontrada",status = status.HTTP_400_BAD_REQUEST)