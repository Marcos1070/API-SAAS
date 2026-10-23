from rest_framework.decorators import api_view      # Trea el decorador @api_view de django rest framework
from rest_framework.response import Response        # Trae el generador de respuetas HTTP de DRF
from rest_framework import status                   # Importa el diccionario de constantes con codigos de respuesta HTTP (200,201,400,etc)

from .models import OrdenTrabajo, Cliente                  # Importa la clase del modelo declarada en models.py
from .serializers import OrdenTrabajoSerializer, ClienteSerializer     # Importa la clase traductora declarada en serializers.py
from rest_framework import generics

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class OrdenTrabajoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
