#sirven para que otras personas o uno mismo instale paquetes en su pc y poder usar sus modulos desde cualquier directorio
#PASOS PARA CREAR UN PAQUETE DISTRIBUIBLE:

'''

1_crear un archivo con nombre setup.py en la raiz de la carpeta(paquete), contiene una descripcion del paquete a distribuir:

	from setuptools import setup

	setup(

		name="nombre del paquete",
		version="se cambia cuando se actualiza el paquete",
		description="que funcion cumple el paquete",
		author="nombre del autor",
		author_email= no es obligatorio,
		url = no obligatorio,
		packages=[ruta donde se encuentra el paquete]

	)

2_ ir hasta la direccion donde se encuentra el archivo setup.py desde la consola
3_ escribir en el directorio python setup.py sdist
4_ se crea un archivo comprimido con el paquete distribuible


#PASOS PARA INTALAR UN PAQUETE DISTRIBUIBLE:

1_desde la consola ir hasta el directorio donde se encuentra el archivo comprimido
2_ escribir pip3 install "nombre del paquete" (con extension de archivo comprimido)

3_para desintalar el paquete desde cualquier directorio de la consonla escribir:
	pip3 uninstall "nombre del paquete" (sin extension)
