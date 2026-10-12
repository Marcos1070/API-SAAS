from rest_framework import serializers                          # Importa el paquete de herramientas de DRF diseñado para la conversion y validacion de datos
from .models import OrdenTrabajo, Cliente                                # Importa el modelo desde el archivo models.py ubicado en la misma carpeta 

class OrdenTrabajoSerializer(serializers.ModelSerializer):      # Crea una clase que hereda de ModelSerializer. Esta clase especial le indica a DRF: No me hagas configurar los campos a mano, lee mi modelo d Django y genera el serializador automaticamente
    class Meta:                                                 # Es una clase interna de configuracion que le da instrucciones precisas a Django/DRF sobre como debe comportarse la clase principal 
        model = OrdenTrabajo                                    # Le dice a la clase Meta exactamente cual es el modelo de la base de datos que debe tomar como plantilla
        fields = '__all__'                                      # Le indica a DRF que incluya todos los campos del modelo en la conversion a JSON. En nuestro caso, incluira automaticamente id, titulo y descripcion. Si mas adelante no se quieren exponer todos los datos de un modelo API, en lugar de '__all__' se puede especificar solo con una lista los campos que te interesan: fields = ['id', 'titulo']



class ClienteSerializer(serializers.ModelSerializer):

    #serializador anidado, usamos el related_name='ordenes' que definimos en el modelo ordentrabajo
    #many=true indica que un cliente puede tener multiples ordenes asociadas
    #read_only=true significa que este campo es solo para lectura (mostrar la ordenes del cliente)
    ordenes = OrdenTrabajoSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellido', 'mail', 'ordenes'] # incluimos las ordenes anidadas junto a los datos del cliente
