contrasenia = input("ingrese contrasenia: ")
cont=0

for i in range(len(contrasenia)):
	if contrasenia[i]==" ":
		cont=1
		break;

if cont!=0 or len(contrasenia)<8:
	print("contrasenia erronea")
else:
	print("contrasenia ok")
