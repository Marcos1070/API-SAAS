from django.urls import path
from .views import lista_de_ordenes, detalle_de_orden, lista_de_clientes, detalle_de_cliente

urlpatterns = [

    #ruta para listar y crear ordenes
    path('ordenes/', lista_de_ordenes.as_view(), name='lista_de_ordenes'),

    #ruta para obtener, editar o eliminar una orden por su id
    path('ordenes/<int:pk>/', detalle_de_orden.as_view(), name='detalle de orden'),


    path('clientes/', lista_de_clientes.as_view(), name='lista_de_clientes'),

    path('clientes/<int:pk>/', detalle_de_cliente.as_view(), name='detalle_de_cliente'),


]