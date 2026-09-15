from rest_framework.decorators import api_view      # Trea el decorador @api_view de django rest framework
from rest_framework.response import Response        # Trae el generador de respuetas HTTP de DRF
from rest_framework import status                   # Importa el diccionario de constantes con codigos de respuesta HTTP (200,201,400,etc)
from .models import OrdenTrabajo                    # Importa la clase del modelo declarada en models.py
from .serializers import OrdenTrabajoSerializer     # Importa la clase traductora declarada en serializers.py


#para listar todas las ordenes (get) y crear una nueva (post)

@api_view(['GET', 'POST'])                          # Le indica a django que esta vista funcional unicamente respondera a peticiones HTTP del tipo get o post, cualquier otro metodo como delete o put sera rechazado automaticamente con un codigo de error 405

def ordenes_list_create_view(request):              # Define la funcion principal que recibe el objeto request con la informacion enviada por el cliente
    
    if request.method == 'GET':                                         # Evalua si el cliente esta pidiendo consultar/obtener datos
        ordenes = OrdenTrabajo.objects.all()                            # Ejecuta una consulta a SQLite por medio del orm trayendo todas las filas existentes en la tabla ordenes_ordentrabajo
        serializer =OrdenTrabajoSerializer(ordenes, many=True)          # Le entrega el listado de objetos al serializador para que los convierta en diccionarios. El parametro many=true es imprescindible para indicarle al serializador que debe iterar sobre un listado/queryset de multiples registros y no sobre un solo elemento
        return Response(serializer.data, status = status.HTTP_200_OK)   # Responde a la peticion enviando el arreglo de ordenes en formato JSON junto con el estado de exito 200 OK


    elif request.method == 'POST':                                              # Evalua si el cliente envio datos para crear un nuevo registro
        serializer = OrdenTrabajoSerializer(data=request.data)                  # extrae la informacion enviada en el cuerpo de la peticion HTTP(request.data) y la asigna al serializador para prepara su procesamiento
        if serializer.is_valid():                                               # Ejecuta las validaciones internas (comprobando limites de caracteres como max_lenght=100, tipos de datos y precencia de campos obligatorios)
            serializer.save()                                                   # Si los datos son correctos, el orm genera la instruccion insert into e insterta fisicamente el registro en la base de SQLite
            return Response(serializer.data, status=status.HTTP_201_CREATED)    # retorna la nueva orden recien creada (con el id autogenerado asignado por la bd) e informa un codigo 201 created
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # si la validacion en is_valid() falla, salta el bloque if y responde un estado 400 bad request adjuntado la expliacion exacta en serializer.error






#vista para obtener (get), actualizar (put) o eliminar (delete) por id 

@api_view(['GET', 'PUT', 'DELETE'])         # Le indica a django rest framework que esta vista acepta tres tipos de operaciones get, put, delete
def orden_detail_view(request, pk):         # defina la funcion. Recibe el objeto request (la peticion entrante) y el argumento pk (primary key o id). Ese numero llega desde la url, por ejemplo "1" en /api/ordenes/1/
    

 #busqueda segura del registro en sqlite
    try:
        orden = OrdenTrabajo.objects.get(pk=pk)  # Le pide al orm que busque en la base de datos la fila unica cuyo id coincida con el pk recibido
    except OrdenTrabajo.DoesNotExist:            # si el cliente pide un id que no existe en sqlite (por ejemplo id 999), en lugar de que el servidor colapse lanzando un error interno 500, capturamos esa excepcion y respondemos limpiamente con un mensaje de error y un codigo 404 not found 
        return Response ({'error': 'la orden de trabajo no existe'}, status=status.HTTP_404_NOT_FOUND)


 #Leer una sola orden
    if request.method == 'GET':                     # evalua si la peticion es para consultar
        serializer = OrdenTrabajoSerializer(orden)  # se le pasa la orden encontrada al serializador para que la trasnforme a JSON. Aca no se usa many=true porque se procesa un unico objeto, no una lista
        return Response(serializer.data, status=status.HTTP_200_OK)  # devuelve el JSON con el codigo de exito 200 OK


 #operacion put (editar/actualizar)
    elif request.method == 'PUT':               # evalua si el cliente envio datos para actualizar
        serializer = OrdenTrabajoSerializer(orden, data=request.data) # clave de la actualizacion: le pasamos dos cosas al serializador: el objeto actual que sacamos de la bd (orden). los nuevos datos que envio el usuario (data=request.data)
        if serializer.is_valid():       # valida que los nuevos datos respeten las reglas del modelo
            serializer.save()           # como le pasamos una orden existente en el paso anterior, el orm sabe que no debe crear una nueva fila, sino ejecutar un update en sqlite sobre el registro actual
            return Response(serializer.data, status=status.HTTP_200_OK)     # si se guardo, retorna la orden con los datos actualizados y estado 200 OK. si fallo la validacion, retorna los errores con codigo 400 bad request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



 #operacion delete
    elif request.method == 'DELETE':        # evalua si la peticion pide borrar el recurso
        orden.delete()              # le ordena al orm ejecutar la instruccion sql delete sobre ese registro en la base de datos
        return Response({'mensaje': 'orden eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)   # devuelve la confirmacion. El estado 204 no content es el estandar de las apis rest para indicar que la eliminacion fue exitosa y que el recurso ya no existe

