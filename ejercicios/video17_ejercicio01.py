num1 = int(input("ingrese numero: "))
num2 = int(input("ingrese numero mayor que "+str(num1)+": "))

while(num2>num1):
	num1=num2
	num2 = int(input("ingrese numero mayor que "+str(num1)+": "))

print("\nnumero menor ingresado, fin del programa")