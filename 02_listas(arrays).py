# a diferencia de otros lenguajes python puede almacenar distintos tipos de datos en un array

miLista=["vicki","rocio","flor", "seba"]

#imprimir toda la lista
print(miLista)

#acceder a un elemento de la lista
print(miLista[3])

#cuando usamos numero negativo empieza a contar desde el final de la lista con el -1
print(miLista[-4]) #imprime vicki

#para acceder al array por partes
print(miLista[0:3]) #imprime del indice 0 al 2
print(miLista[2:]) #imprime del indice 1 hasta el final de la lista

#para agregar un elemento al final de la lista se usa el .append
miLista.append("lucas")
print(miLista)

#para agregar un elemento en un indice especifico de la lista se utiliza .insert(indice,elemento)
miLista.insert(2,"abril")
print(miLista)

#para agregar varios elementos a la lista se utiliza .extend([elementos])
miLista.extend(["sandra","ana","lucia"])
print(miLista)

#devuelve en que indice se encuentra un elemento de la lista .index(elemento)
#si el elemento esta repetido, siempre devuelve el indice del primer elemento
print(miLista.index("abril"))

#comprueba si un elemento existe dentro de la lista, devuelve true/false
print("pepe" in miLista)

#para remover un elemento de la lista .remove(elemento)
miLista.remove("abril")
print(miLista)

#para eliminar ultimo elemento .pop()
miLista.pop()
print(miLista)

#operador + se utiliza para sumar listas entre si
miLista1 = ["hola","mundo"]
miLista2=["hello","world"]
miLista3=miLista1+miLista2
print(miLista3)

#agregar el operador * al final de la lista permite especificar la cantidad de veces que se quiere que se repita la lista
ejemplo=["rocio","diaz"] *4
print(ejemplo)