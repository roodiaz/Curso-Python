#diferencias con los arrays:

#se declaran con () en vez de []
#una vez declarada no se puede modificar(append, extend, remove)
#permite extraer porciones, pero el resultado de esa extraccion es una tupla nueva
#son mas rapidas, ocupan menos espacio, puede usarse como claves en un diccionario

miTupla=(4,7,6,2,5,2)

print(miTupla[2])

#metodo conversion tupla a lista
miLista=list(miTupla)

#metodo conversion lista a tupla
miLista1=['a','b','p']
miTupla1=tuple(miLista1)

#verificar si existe elemento en tupla
print(4 in miTupla)

#contar cantidad de elementos iguales especificados .count()
print(miTupla.count(2))

#contar cantidad total de elementos en tupla .len()
print(len(miTupla))

#se puden declarar tuplas unitarias, se debe agregar una , al final
miTuplaUni = ("juan",) 

#desempaquetado de tuplas permita guardar un elemento de una tuplar en una variables
tupla=(18,5,2020)
dia, mes, anio =tupla #las guarda por orden
print(dia, mes, anio)