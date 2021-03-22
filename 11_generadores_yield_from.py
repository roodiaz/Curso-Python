#se usa para simplificar el codigo de los generadores al trabajar con bucles anidados
#ej: si tengo un objeto cargado con listas, acceder al contenido de una de ellas 

#generador normal
def generadorCiudades(*ciudades): #* delante del argumento indica que va a recibir un numero indeterminado de elementos y en forma de tuplas
	for elemento in ciudades:
		yield elemento #devuelve elemento 


ciudades = generadorCiudades("madrid","barcelona","bilbao","valencia")

print(next(ciudades))
print(next(ciudades))
print()


def generadorCiudades_(*ciudades):
	for elemento in ciudades:
		for subElemento in elemento:
			yield subElemento #devuelve subElemento(letras) del elmento ciudades


ciudades = generadorCiudades_("madrid","barcelona","bilbao","valencia")

print(next(ciudades))
print(next(ciudades))
print()


#generador con yield from simplificado, permite prescindir del bucle anidado
def generadorCiudades_1(*ciudades):
	for elemento in ciudades:
		#for subElemento in elemento:
			yield from elemento #devuelve subElemento(letras) del elmento ciudades


ciudades = generadorCiudades_1("madrid","barcelona","bilbao","valencia")

print(next(ciudades))
print(next(ciudades))