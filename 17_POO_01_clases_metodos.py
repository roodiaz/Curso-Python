class Coche():

#atributos(propiedades)
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enMarcha=False

#metodos(comportamientos)
	def arrancar(self): #self = this de c#
		self.enMarcha=True

	def  estado(self):
		if self.enMarcha:
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"


#instanciar una clase(crear un objeto de la clase)
miCoche=Coche()

print(miCoche.largoChasis)
print(miCoche.estado())
miCoche.arrancar()
print(miCoche.estado())