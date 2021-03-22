def evaluacion(nota):
	return "aprobado"
	if nota<4:
		return "desaprobado"


notaAlumno=input("ingrese nota: ")
print(evaluacion(notaAlumno))

#los datos ingresados como teclado python los toma como string
#para convertir tipo de dato string a int print(evaluacion(int(notaAlumno)))
#con la nueva actualizacion 3.8 ya no es necesario hacer casteo del dato ingresado!!!!