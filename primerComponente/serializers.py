from rest_framework import routers, serializers, viewsets

#Importancion de modelos
from primerComponente.models import PrimerTabla

class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerTabla
        # fields = ('pk','nombre', 'edad')
        fields = ('pk','__all__')