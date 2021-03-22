
print("PROGRAMA DE BECAS\n")

distanciaEscuela = int(input("introduce la distancia la escuela en km: "))
cantidadHermanos = int(input("ingrese cantidad de hermanos: "))
salarioFamiliar = float(input("ingrese salario anual bruto: "))

#si las dos primeras condiciones no se cumplen, pero el salario es menor a 20000 entra en el if
if distanciaEscuela>40 and cantidadHermanos>2 or salarioFamiliar<=20000:
	print("tienes derecho a beca")
else:
	print("no tienes derecho a beca")



print("\n\nPROGRAMA ELECCION DE MATERIA OPTATIVA\n")

listaMaterias={1:"programacion",2:"laboratorio",3:"sistemas operativos"}
print("Materias disponibles: \n1.programacion\n2.laboratorio\n3.sistemas operativos")
eleccion = int(input("\ningrese numero de la materia escogida: "))

if eleccion in (1,2,3):
	print("la materia escogida es "+listaMaterias[eleccion])
else:
	print("materia no disponible")


