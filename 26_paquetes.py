#los paquetes son directorios donde se almacenan modulos relacionados entre si, 
#sirven para organizar y reutilizar codigos

'''pasos para crear paquetes:

1_ crear una carpeta con el nombre del paquete que quieras ejemplo 'vehiculos'
2_ crear dentro un archivo con el nombre __init__.py
3_ guardar modulos necesarios ejemplo: 'autos', 'motos'
4_ para utilizar el paquete fuera de la carpeta se utiliza el '.' ejemplo:

  from 'nombre del paquete(carpeta)."nombre del modulo a utilizar" import metodo(s) deseada'
  from 'nombre del paquete(carpeta)."nombre del modulo a utilizar" import * (* importa todos los metodos del modulo)

!!!se pueden crear paquetes dentro de paquetes, se invocan con el mismo criterio del '.' para acceder a las carpetas