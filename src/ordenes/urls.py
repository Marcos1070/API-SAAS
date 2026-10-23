from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, OrdenTrabajoViewSet


# se instancia el DefaultRouter
router = DefaultRouter()

#registramos nuestros ViewSets
router.register(r'clientes', ClienteViewSet, basename = 'cliente')
router.register(r'ordenes', OrdenTrabajoViewSet, basename = 'ordentrabajo')

#incluimos las rutas generadas por el router en el urlpatterns

urlpatterns = [

    path('', include(router.urls))

]