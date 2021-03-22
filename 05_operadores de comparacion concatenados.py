salarioPresidente = int(input("ingrese salario presidente: "))
salarioDirector = int(input("ingrese salario director: "))
salarioJefeArea = int(input("ingrese salario jefe de area: "))
salarioAdministrativo = int(input("ïngrese salario administrativo: "))

if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
	print("todo ok")
else:
	print("todo mal")