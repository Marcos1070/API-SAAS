from rest_framework.decorators import api_view      # Trea el decorador @api_view de django rest framework
from rest_framework.response import Response        # Trae el generador de respuetas HTTP de DRF
from rest_framework import status                   # Importa el diccionario de constantes con codigos de respuesta HTTP (200,201,400,etc)

from .models import OrdenTrabajo, Cliente                  # Importa la clase del modelo declarada en models.py
from .serializers import OrdenTrabajoSerializer, ClienteSerializer     # Importa la clase traductora declarada en serializers.py
from rest_framework import generics



#remplazo de ordenes_list_create_view
class lista_de_ordenes(generics.ListCreateAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer


#remplazo de orden_detail_view
class detalle_de_orden(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer



#para cliente
class lista_de_clientes(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class detalle_de_cliente(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
