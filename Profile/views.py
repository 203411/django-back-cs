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

    def get_user(self, id_user,format=None):
        try:
            return User.objects.get(pk = id_user)
        except User.DoesNotExist:
            return 404
    
    def post(self, request,format=None):
        if 'url_img' not in request.data:
            raise exceptions.ParseError(
                "No has seleccionado el archivo a subir")
        user = self.get_user(request.data['id_user'])
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
            return Response("User doesn't exist")
    
class ProfileTableDetail(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(id_user = pk)
        except Profile.DoesNotExist:
            return 404
    
    def get(self, request, pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 404:
            id_response = ProfileSerializer(id_response)
            return Response(id_response.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        archivos = request.data['url_img']
        id_response = self.get_object(pk)
        if(id_response != 404):
            try:
                os.remove('assets/'+str(id_response.url_img))
            except os.error:
                print("La imagen no existe")
            id_response.url_img = archivos
            id_response.save()
            return Response("Todo bien",status.HTTP_201_CREATED)
        else:
            return Response("No salio bien")
    
    def delete(self, request, pk):
        profile = self.get_object(pk)
        if profile != 404:
            profile.url_img.delete(save=True)
            return Response("Imagen eliminada",status=status.HTTP_204_NO_CONTENT)
        return Response("Imagen no encontrada",status = status.HTTP_400_BAD_REQUEST)
    
class UserProfile(APIView):
    
    def res_custom(self, user):
        response = {
            "first_name" : user[0]['first_name'],
            "last_name" : user[0]['last_name'],
            "username" : user[0]['username'],
            "email" : user[0]['email']
        }
        return response
    
    def get(self, request, pk, format=None):
        user = User.objects.filter(pk=pk)
        if(user != 404):
            response_data = self.res_custom(user.values())
            return Response(response_data, status= status.HTTP_200_OK)
        else:
            return Response("User does not exist", status = status.HTTP_404_NOT_FOUND)
        
    
    def put(self, request, pk, format=None):
        data = request.data
        user = User.objects.filter(pk = pk)
        if(user != 404):
            user.update(username = data.get('username'))
            user.update(first_name = data.get('first_name'))
            user.update(last_name = data.get('last_name'))
            user.update(email = data.get('email'))
            return Response(self.res_custom(user.values()), status = status.HTTP_200_OK)
        else:
            return Response("User does not exist", status = status.HTTP_400_BAD_REQUEST)

        