#ENCAPSULAMIENTO DE METODOS:
"""doble _ sirve para encapsular metodos y no permitir que se modifique fuera de la 
   clase, debe ponerse doble _ en todas las llamadas de los metodos encapsulados"""

"""doble _ sirve para encapsular atributos y no permitir que se modifique fuera de la 
   clase, debe ponerse doble _ en todas las llamadas de los atributos encapsulados"""

class Coche():

	#constructores
	def __init__(self):
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4 
		self.__enMarcha=False
		"""doble _ sirve para encapsular atributos y no permitir que se modifique fuera de la 
		   clase, debe ponerse doble _ en todas las llamadas de los atributos encapsulados"""

	#metodos(comportamientos)
	def arrancar(self,arrancamos): #self = this de c#
		self.__enMarcha=arrancamos

		if self.__enMarcha:
			chequeo=self.__chequeoInterno()
		if self.__enMarcha and chequeo:
			return "El coche esta en marcha"
		elif self.__enMarcha and chequeo == False:
			return "Algo ha ido mal en el chequeo"
		else:
			return "El coche esta parado"


	def estado(self):
		print("Cantidad de ruedas ",self.__ruedas)
		print("Largo del chasis ",self.__largoChasis)
		print("Anco del chasis ",self.__anchoChasis)


	"""doble _ sirve para encapsular metodos y no permitir que se modifique fuera de la 
		clase, debe ponerse doble _ en todas las llamadas de los metodos encapsulados"""
	def __chequeoInterno(self):
		print("realizando chequeo interno...")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
			return True
		else:
			return False

# ------------------------- FIN DE LA CLASE -------------------------------- #

#instanciar una clase(crear un objeto de la clase)
print("*** Primer objeto ***")
miCoche=Coche()
miCoche.estado()
print(miCoche.arrancar(True))

