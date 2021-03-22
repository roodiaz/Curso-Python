#lanzamiento de excepciones: provocar un error de forma intencionada
#se utiliza la instruccion Raise


def evaluaEdad(edad):

	if edad<0:
		raise TypeError("no se permiten edades negativas")

	if edad<20:
		return "eres menor de edad"
	elif edad<40:
		return "eres de edad media"
	elif edad<65:
		return "eres casi viejo"
	else:
		return "tas para el cajon"

print(evaluaEdad(-18))