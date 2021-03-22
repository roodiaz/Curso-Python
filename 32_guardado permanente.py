import pickle

class Persona:

	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("se ha creado una persona nueva con el nombre de ",self.nombre)

	#convierte en cadena de txt info de un objeto
	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

    #  ----------------------------------------------------------------  #

class ListaPersonas:

	personas=[]

	#creo constructor que guarde fichero cada vez que se inicializa
	def __init__(self):

		listaDePersonas=open("ficheroPersona","ab+")
		listaDePersonas.seek(0)

		try:
			self.listaDePersonas=pickle.load(listaDePersonas)
			print("se cargaron {} personas del fichero externo".format(len(self.personas)))

		except:

			print("el fichero esta vacio")

		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def savePersona(self,p):
		self.personas.append(p)
		self.savePersonaEnFicheroExt()

	def loadPersona(self):
		for p in self.personas:
			print(p)

	def savePersonaEnFicheroExt(self):
		listaDePersonas=open("ficheroPersona","wb")
		pickle.dump(self.personas,listaDePersonas)
		listaDePersonas.close()
		del(listaDePersonas)


  	#  ----------------------------------------------------------  #


miLista=ListaPersonas()
p=Persona("lucas","m",25)
miLista.savePersona(p)
