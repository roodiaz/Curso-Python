#son errores en tiempo de ejecucion que hace que no se termine de ejecutar todas las lineas de codigo
#la sintaxis del codigo es correcta pero durante la ejeccucion ocurre "algo inesperado"
#esos errores se puede controlar para que la ejecucion del programa termine, se lo conoce como "manejo o control de exepciones"


#en este codigo si haces division por 0 salta un error
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	try:                    #bloque try/except se usa para controlar error en linea de codigo para divisiones entre 0
		return num1/num2  
	except ZeroDivisionError: #"ZeroDivisionError" es el error que frena la ejecucion del programa
		print("no se puede dividir entre 0") #hace excepcion del error y muestra mensaje en vez de frenar programa
		return "operacion invalida"
	

op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")
