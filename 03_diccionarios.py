#estructura de datos que permite almacenar diferentes tipos de dato, lista y otros dicccionarios
#se crean con asociacion clave/valor(clave es un valor unico e irrepetible)
#lo elementos almacenados no estan ordenados
#se declaran entre {}

miDiccionario={"alemania":"berlin","francia":"paris","reino unido":"londres","espania":"madrid"}
print(miDiccionario["francia"]) #se accede al valor(capital) a traves de la clave(pais)

#agregar elementos a un diccionario,se declara la clave entre []
miDiccionario["italia"]="lisboa"

#modificar valor, solo hay que sobreescribir el valor
miDiccionario["italia"]="roma"

#eliminar elemento, primero va la palabra reservada del despues el nombre del diccionario y entre [] la clave del valor a eliminar 
del miDiccionario["reino unido"]

#utilizar tuplas para asignar claves a los valores
miTupla=("espania","francia","italia","alemania")
miDiccionario1={miTupla[0]:"madrid",miTupla[1]:"paris",miTupla[2]:"roma",miTupla[3]:"berlin"}

#almacenar una tupla en un dicc
miDiccionario2={23:"jordan","nombre":"michael","equipo":"chicago","anillos":(1991,1992,1993,1996,1997,1998)} #asignar en clave anillos mas de un valor

#almacenar un dicc dentro de otro dicc
miDiccionario3={23:"jordan","nombre":"michael","equipo":"chicago","anillos":{"temporadas":(1991,1992,1993,1996,1997,1998)}}

#metodos
.keys() #devuelve solo las claves
.values() #devuelce solo los valores
len(miDiccionario) #devuelve longitud del dicc
miDiccionario.update(miDiccionario1) #une dos diccionarios