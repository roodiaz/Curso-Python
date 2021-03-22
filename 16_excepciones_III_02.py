import math

def calculaRaiz(num):
 	if num<0:
 		raise ValueError("el numero no puede ser negativo")
 	else:
 		return math.sqrt(num)


op1=(int(input("introduce un numero: ")))

try:
	print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)

print("programa terminado")