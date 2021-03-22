mail = input("ingrese mail: ")
contArroba=0
contPunto=0

for i in mail:
	if i==" ":
		break;
	if i=="@":
		contArroba+=1
	if i==".":
		contPunto+=1

if contArroba==1 and contPunto>0:
	print("mail correcto")
else:
	print("mail incorrecto")

