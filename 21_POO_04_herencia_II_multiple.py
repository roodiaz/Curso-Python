#HERENCIA MULTIPLE
#SOBRE ESCRITURA DE METODOS

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



class VElectricos():

	def __init__(self):
		self.autonomia=100

	def CargaEnergia(self):
		self.cargando=True

	             #---------------- Fin clase vehiculos electricos ---------------#



#clase que hereda de una clase (vehiculos)
class Moto(Vehiculos):

	willie=""

	def Willie(self):
		self.willie="Voy haciendo la willie ndea"

	#sobre escribo metodo usando mismo nombre de metodo pero agregandole linea de codigo que sea necesaria
	def Estado(self):
		print("Marca: ",self.marca, "\nModelo: ",self.modelo,"\nEn marcha: ",self.enMarcha,
			"\nAcelerar: ",self.acelera,"\nFrenar: ",self.frena,"\n",self.willie)

                #---------------- Fin clase moto ---------------#


#clase que hereda de una clase (vehiculos)
class Furgoneta(Vehiculos):

	def Carga(self,cargar):
		self.cargado=cargar

		if self.cargado:
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta no esta cargada"

                #---------------- Fin clase furgoneta ---------------#

#clase que hereda de dos clases(vehiculos y velectricos), herencia multiple
class BiciElectrica(VElectricos,Vehiculos):
	pass



	            #---------------- Fin clase bici electrica ----------------#

miMoto=Moto("Honda","CBR")
miMoto.Willie()
#cuando se llama un metodo sobreescrito,siempre se sobreescribe el metodo que heredes de la clase padre 
#por ende se llamaria al metodo de la clase que hereda, en este caso la clase Moto()
miMoto.Estado()

print()

miFurgo=Furgoneta("Renault","Kangoo")
miFurgo.Arrancar()
miFurgo.Estado()
print(miFurgo.Carga(True))

print()

#miBici=BiciElectrica("Orbea","HTC1000") 
"""salta error porque la declaracion de la clase BiciElectrica posee herencia multiple y python le da preferencia
   a la primera clase declarada en los parametros, en este caso la clase VElectricos que tiene un constructor sin
   parametros. Si invierto los parametros de la clase BiciElectrica tomaria el constructor de Vehiculos