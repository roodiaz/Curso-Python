
print("*** Programa de astrologia ***\n\n")
print("Ingrese fecha de nacimiento \n")

while True:
	try:
		dia=int(input("dia: "))
		while dia>31 or dia<0:
			dia=int(input("invalido, reingrese dia: "))

		mes=int(input("mes: "))
		while mes>12 or mes<0:
			mes=int(input("invalido, reingrese mes: "))
		break;
	except ValueError:
		print("valores introducidos invalidos, intente nuevamente\n")

print()

signo=("capricornio","acuario","piscis","aries","tauro","geminis","cancer","leo","virgo","libra", "escorpio","sagitario")
fecha=(20,19,20,20,20,21,23,23,23,22,22,21)#fechas en las que termina cada signo empezando por enero

mes=mes-1 #le resto un mes porque los indices van de 0 a 11

if(dia>fecha[mes]): #verifico que no se pase de la fecha dentro del indice
	mes = mes+1 #aumento un indice, ej: si el dia del mes de enero se pasa del 20 deja de ser capricornio y pasa a ser acuario 
if mes==12: 
	mes=0 #si se pasa del indice 11 vuelve al 0

print("tu signo es ",signo[mes])

#FORMA LARGA:

"""if  mes==12 and dia in range(22,31) or mes==1 and dia in range(1,20) :
	print("tu signo es capricornio")
elif mes==1 and dia in range(21,31) or mes==2 and dia in range(1,19):
	print("tu signo es acuario")
elif mes==2 and dia in range(20,29) or mes==3 and dia in range(1,20):
	print("tu signo es piscis")
elif mes==3 and dia in range(21,31) or mes==4 and dia in range(1,20):
	print("tu signo es aries")
elif mes==4 and dia in range(21,30) or mes==5 and dia in range(1,20):
	print("tu signo es tauro")
elif mes==5 and dia in range(21,31) or mes==6 and dia in range(1,21):
	print("tu signo es geminis")
elif mes==6 and dia in range(22,30) or mes==7 and dia in range(1,23):
	print("tu signo es cancer")
elif mes==7 and dia in range(24,31) or mes==8 and dia in range(1,23):
	print("tu signo es leo")
elif mes==8 and dia in range(24,31) or mes==9 and dia in range(1,23):
	print("tu signo es virgo")
elif mes==9 and dia in range(24,30) or mes==10 and dia in range(1,22):
	print("tu signo es libra")
elif mes==10 and dia in range(23,31) or mes==11 and dia in range(1,22):
	print("tu signo es escorpio")
else:
	print("tu signo es sagitario")"""
