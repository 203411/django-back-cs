from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime

#Importaciones de modelos
from primerComponente.models import PrimerTabla

#Importaciones de serializadores
from primerComponente.serializers import PrimerTablaSerializer

# Create your views here.
class PrimerTablaList(APIView):
    #Funciona aun sin el json.dumps y sin el json.loads
    def response_custom(self,messages,pay_load, status):
        response_json = {"messages":messages,"pay_load":pay_load,"status":status}
        return response_json
    
    def get(self, request, format=None):
        queryset = PrimerTabla.objects.all()
        serializer = PrimerTablaSerializer(queryset, many = True, context = {'request':request})
        return Response(self.response_custom("Success",serializer.data, status.HTTP_200_OK))
    
    def post(self, request, format=None):
        serializer = PrimerTablaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(self.response_custom("Success", datas,  status.HTTP_201_CREATED))
        return Response(self.response_custom("Error",serializer.errors,status.HTTP_400_BAD_REQUEST))
    
class PrimerTablaDetail(APIView):
    def get_object(self, pk):
        try:
            return PrimerTabla.objects.get(pk = pk)
        except PrimerTabla.DoesNotExist:
            return 0
        
    def get(self, request,pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response = PrimerTablaSerializer(id_response)
            return Response(id_response.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,pk, format=None):
        id_response = self.get_object(pk)
        serializer = PrimerTablaSerializer(id_response, data = request.data)
        request.data['edited'] = datetime.datetime.now()
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response.delete()
            return Response("Dato eliminado", status = status.HTTP_201_CREATED)
        return Response("Dato no encontrado",status = status.HTTP_400_BAD_REQUEST)
    