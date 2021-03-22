def obtenerMax(num1, num2):
	if num1>num2:
		return num1
	elif num1<num2:
		return num2
	else:
		return "son iguales"

num1 = input("ingrese primer numero: ")
num2 = input("ingrese segundo numero: ")

print("numero mayor: ",obtenerMax(num1,num2))