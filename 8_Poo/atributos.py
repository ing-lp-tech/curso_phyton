class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
luis=Persona("luis",32)

print(luis.nombre)
print(luis.edad)