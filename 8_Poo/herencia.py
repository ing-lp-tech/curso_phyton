class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleaños {self.edad} {self.nombre}")

class Empleado(Persona):
    def __init__(self, nombre, edad, horas_totales):
        """ super().__init__(nombre, edad)  """ # Llama al constructor de la clase base
        super(Empleado,self).__init__(nombre, edad)
        self.horas_totales = horas_totales

    def trabajar(self, horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print(f"Usted ha trabajado {horas_trabajadas} horas")
        print(f"Horas totales: {self.horas_totales}")

# Crear una instancia de Empleado
luis = Empleado(nombre="Luis", edad=32, horas_totales=40)
luis.trabajar(horas_trabajadas=8)
luis.cumplir_anios()

""" class Persona:

    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def cumplir_anios(self):
        self.edad+=1
        print(f"feliz cumpleaños {self.edad} {self.nombre}")

class Empleado(Persona):
    def __init__(self,horas_totales):
        self.horas_totales=horas_totales
    

    def trabajar(self,horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print(f"Usted ha trabajado {horas_trabajadas} horas")
        print(f"Horas totales: {self.horas_totales}")

        
luis=Empleado(nombre="luis",edad=32,horas_totales=40)
luis.trabajar(horas_trabajadas=8)
luis.cumplir_anios()
 """