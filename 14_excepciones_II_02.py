#esta funcion presenta dos excepciones 
#python permite capturar varias excepciones
#todo lo que se introduzca dentro de la instruccion finally se va a ejecutar ocurra o no una excepcion

def divide():
	try:
		num1=float(input("Ingrese el primer numero: "))
		num2=float(input("Ingrese el segundo numero: "))

		print("La division es: ", num1/num2)
	except ValueError:
		print("\nValor ingresado invalido")
	except ZeroDivisionError:
		print("\nNo se puede dividir entre 0")

	print("Calculo finalizado\n")


divide()

#tambien se puede hacer una excepcion general sin especificar error pero es una mala practica
def divide():
	try:
		num1=float(input("Ingrese el primer numero: "))
		num2=float(input("Ingrese el segundo numero: "))

		print("La division es: ", num1/num2)
	except:
		print("\nHa ocurrido un error")

	finally:
		print("Calculo finalizado")


divide()