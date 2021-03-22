import pickle
from io import open

class Vehiculos():

	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enMarcha=False
		self.acelera=False
		self.frena=False

	def Arrancar(self):
		self.enMarcha=True

	def Acelerar(self):
		self.acelera=True

	def Frenar(self):
		self.frena=True

	def Estado(self):
		print("Marca: ",self.marca, "\nModelo: ",self.modelo,"\nEn marcha: ",self.enMarcha,
			"\nAcelerar: ",self.acelera,"\nFrenar: ",self.frena)

#creo 3 objetos
coche1=Vehiculos("audi","r8")
coche2=Vehiculos("bmw","i8")
coche3=Vehiculos("porsche","911")

coches=[coche1,coche2,coche3]
save_fichero=open("obj_coches","wb")
pickle.dump(coches,save_fichero)
save_fichero.close()
del(save_fichero)


open_fichero=open("obj_coches","rb")
misCoches=pickle.load(open_fichero)
open_fichero.close()

for i in misCoches:
	print(i)

for i in misCoches:
	print(i.Estado())