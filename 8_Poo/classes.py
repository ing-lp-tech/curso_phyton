class Persona:

    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def cumplir_anios(self):
        self.edad+=1
        print(f"feliz cumpleaños {self.edad} {self.nombre}")


        
luis=Persona("luis",32)

luis.cumplir_anios()
