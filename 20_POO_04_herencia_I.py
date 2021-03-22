#HERENCIA

#clase padre
class Vehiculos():

	#constructor padre
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enMarcha=False
		self.acelera=False
		self.frena=False


	#metodos padre
	def Arrancar(self):
		self.enMarcha=True

	def Acelerar(self):
		self.acelera=True

	def Frenar(self):
		self.frena=True

	def Estado(self):
		print("Marca: ",self.marca, "\nModelo: ",self.modelo,"\nEn marcha: ",self.enMarcha,
			"\nAcelerar: ",self.acelera,"\nFrenar: ",self.frena)

                 #---------------- Fin clase padre ---------------#

#clase que hereda
class Moto(Vehiculos):
	pass



miMoto=Moto("Honda","CBR")
miMoto.Estado()