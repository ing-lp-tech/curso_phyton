class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad


luis=Persona("luis",32)

print(luis.nombre)
print(luis.edad)


""" atributo: Este es un atributo de clase (también conocido como atributo estático). Se declara fuera del método __init__ y es compartido entre todas las instancias de la clase. En este caso, atributo tiene un valor de 123.
nombre y edad: Estos son atributos de instancia. Se definen dentro del método __init__ y son específicos para cada instancia individual de la clase. Cada objeto de la clase Persona tendrá su propio valor para nombre y edad.
En resumen:

atributo: Atributo de clase compartido entre todas las instancias.
nombre y edad: Atributos de instancia específicos para cada objeto creado a partir de la clase Persona. """