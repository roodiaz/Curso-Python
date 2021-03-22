# bucle determinado, sintaxis: for 'variable' in 'elemento a recorrer'

for i in ["rocio","lucas","seba"]:
	#palabra reservada end sirve para indicar como se quiere que termine cada linea evitando el salto de linea
	print("hola", end=" ") #muestra hola tres veces porque la lista tiene tres valores
	print(i) #imprime los valores de la lista que se va almacenando en la variable i
	

print()

cont = 0
miMail=input("ingrese mail: ")

for i in miMail:
	if i=="@" or i=="." :
		cont=cont+1
		

if cont==2:
	print("mail correcto")
else:
	print("mail incorrecto")


print()

for i in range(3):
	print(i)

#el bucle range() admite hasta 3 parametros donde el primero es el punto de inicio, el segundo donde termina 
#y el tercero de cuanto en cuanto tiene que contar ejemplo:
# (1,100,2) va del 1 al 100 contando de 2 en 2