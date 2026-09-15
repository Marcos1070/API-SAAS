from django.db import models                    # Importa el modulo de django que contiene las herramientas para interactuar con la base de datos sin escribir SQL

class OrdenTrabajo(models.Model):               # Definimos el modelo, al poner (models.Model) entre parentesis, le indicamos a django que esta clase no es un objeto comun de python, sino una tabla de base de datos 
    titulo = models.CharField(max_length=100)   # Se crea una columna llamada titulo, el CharField es una cadena de texto con una longitud de hasta 100 caracteres
    descripcion = models.TextField()            # Se crea la columna descripcion con un TextField que es una cadena de textos con una longitud sin limite establecido

    def __str__(self):                          # Define como se debe mostrar este objeto cuando se imprime en consola o en el panel de administracion de django
        return self.titulo                      # Le indica que al representar la orden, muestre su titulo (ej: Reparacion de cañerias) en lugar de mostrar algo como <OrdenTrabajo (1) object>

