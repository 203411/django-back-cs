from django.shortcuts import render

# Importaciones
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        