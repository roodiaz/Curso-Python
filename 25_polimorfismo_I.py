#POLIMORFISMO:
"""un objeto puede cambiar de forma depende del contexto en el que se utilize, al cambiar de forma cambia de comportamiento"""

class Coche():

	def Desplazamiento(self):
		print("me desplazo usando 4 ruedas")


class Moto():

	def Desplazamiento(self):
		print("me desplazo usando 2 ruedas")


class Camion():

	def Desplazamiento(self):
		print("me desplazo usando 6 ruedas")


#el objeto vehiculo puede cambiar de forma
def DesplazamientoVE(vehiculo):
	vehiculo.Desplazamiento()


miMoto=Moto()
DesplazamientoVE(miMoto)

miCamion=Camion()
DesplazamientoVE(miCamion)