''''
#permite almacenar en archivos externos los datos con los que se estuvieron trabajando en la ejecucion del programa
#hay dos alternativas para guardar datos:
	1_en archivos externos(.bin, .txt)
	2_trabajo con BBDD(bases de datos)

#fases para guardar info
	1_crear archivos
	2_abrir
	3_escribir/leer
	4_guardar/cerrar

 PARA MANEJAR ARCHIVOS SE UTILIZA EL MODULO .io

'''
from io import open

#open() lleva dos parametros, el nombre del archivo y el modo en que se abre el archivo
#modo lectura(r), escritura(w), append(a)
#sino existe el archivo la funcion open() lo crea
archivo_texto=open("archivo.txt","w")
archivo_texto.write("Hello world \nrocio la + kpita")
archivo_texto.close()

#leer texto
archivo_texto=open("archivo.txt","r")
texto=archivo_texto.read()
archivo_texto.close()
print(texto)


print()
#la funcion readlines() guardar el archivo en una lista
archivo_texto=open("archivo.txt","r")
lista=archivo_texto.readlines()
archivo_texto.close()
print(lista)
print(lista[0])
print(lista[1])


#appende sirve para agregar texto al ya existente
archivo_texto=open("archivo.txt","a")
archivo_texto.write("\nestoy ebria ndea")
archivo_texto.close()