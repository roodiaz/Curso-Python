from io import open 

texto = open("archivos II.txt","r+")#r+ lectura/escritura
texto.write("texto de prueba")

#metodo seek() lleva como parametro el numero de caracter donde se desea 
#posicionar el cursor en el texto
 
print(texto.read())
texto.seek(5)
print(texto.read())
texto.seek(0)#hace que el cursor vuelva al indice 0 despues de leer el txt

#el metodo read() lleva como parametro el numero de caracter hasta donde se
#desea leer el texto
print(texto.read(6))
texto.seek(0)


texto.seek(len(texto.read())/2)#coloca puntero a mitad del texto
print(texto.read())
texto.close()
