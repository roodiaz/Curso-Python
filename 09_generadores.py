#se declaran igual que las funciones pero usa la palabra reservada yield
#son mas eficientes y gastan menos recursos que las funciones
#duvuelve un objeto con el primer valor almacenado
#almacena valores de uno en uno

#funcion normal
def generaPares(limite):
	miLista=[]

	for i in range(1,limite+1):
		if i%2==0:
			miLista.append(i)

	return miLista

print(generaPares(6))
print()


#generador
def generaPares1(limite):
	for i in range(1,limite+1):
		if i%2==0:
			yield i


devuelvePares=generaPares1(6) #creo un objeto para almacenar lo que devuelve el generador

for i in devuelvePares: #creo un bucle para recorrer el objeto iterable
	print(i,end=" ")


#la funcion next() devuelve el siguiente elemento en la secuencia
print(next(devuelvePares)) #imprime primer elemento del objeto
print(next(devuelvePares)) #imprime segundo elemento del objeto
print(next(devuelvePares)) #imprime tercer elmento del obejeto