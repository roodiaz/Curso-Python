#ENCAPSULAMIENTO DE ATRIBUTOS:

class Coche():

#constructores
	def __init__(self):
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4 
		self.__enMarcha=False
		#poner dos _ sirve para encapsular y no permitir que se modifique fuera de la clase

#metodos(comportamientos)
	def arrancar(self,arrancamos): #self = this de c#
		self.__enMarcha=arrancamos

		if self.__enMarcha:
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"

		self.__enMarcha=True

	def estado(self):
		print("Cantidad de ruedas ",self.__ruedas)
		print("Largo del chasis ",self.__largoChasis)
		print("Anco del chasis ",self.__anchoChasis)
		
# ---------------------------------------------------------------------

#instanciar una clase(crear un objeto de la clase)
print("*** Primer objeto ***")
miCoche=Coche()
miCoche.estado()
print(miCoche.arrancar(True))


print("\n*** Segundo objeto ***")
miCoche2=Coche()
miCoche2.estado()
print(miCoche2.arrancar(False))
