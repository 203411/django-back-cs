from django.shortcuts import render

# Importaciones
from rest_framework.views import APIView
from rest_framework import generics

# Create your views here.

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
class RegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


#     def post(self, request):
#         serializer = RegisterSerializer(data = request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        