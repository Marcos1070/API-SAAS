from django.urls import path
from .views import ordenes_list_create_view, orden_detail_view

urlpatterns = [

    #ruta para listar y crear ordenes
    path('ordenes/', ordenes_list_create_view, name='ordenes-list-create'),

    #ruta para obtener, editar o eliminar una orden por su id
    path('ordenes/<int:pk>/', orden_detail_view, name='orden-detail'),

]