from django.db import models                    # Importa el modulo de django que contiene las herramientas para interactuar con la base de datos sin escribir SQL

#anteriormenete primero estaba "OrdenTrabajo" pero para que ambos se relacionen primero tiene que existir cliente

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    mail = models.EmailField(max_length=100)    

    def __str__(self):
        return f'{self.nombre} {self.apellido}'




#una vez que tenemos la clase cliente ya existiendo podemos recien ahi crear ordentrabajo y hacer la relacion

class OrdenTrabajo(models.Model):               # Definimos el modelo, al poner (models.Model) entre parentesis, le indicamos a django que esta clase no es un objeto comun de python, sino una tabla de base de datos 
    titulo = models.CharField(max_length=100)   # Se crea una columna llamada titulo, el CharField es una cadena de texto con una longitud de hasta 100 caracteres
    descripcion = models.TextField()            # Se crea la columna descripcion con un TextField que es una cadena de textos con una longitud sin limite establecido


    #relacion con el cliente 
    cliente = models.ForeignKey(
        Cliente,    #le indica a dejango a que modelo se esta conectando (por eso tiene que existir antes)
        on_delete=models.CASCADE,    #si se elimina un cliente tambien se eliminara su orden de trabajo
        related_name = 'ordenes', # es el nombre que se le asigna para la relacion entre los clientes y sus ordenes y viceversa
        null = True, # tanto null como blank se utilizan porque ya se crearon ordenes anteriores que no tenian un cliente (solo en este caso)
        blank = True # tanto null como blank se utilizan porque ya se crearon ordenes anteriores que no tenian un cliente (solo en este caso)
    )


    def __str__(self):                          # Define como se debe mostrar este objeto cuando se imprime en consola o en el panel de administracion de django
        return self.titulo                      # Le indica que al representar la orden, muestre su titulo (ej: Reparacion de cañerias) en lugar de mostrar algo como <OrdenTrabajo (1) object>


