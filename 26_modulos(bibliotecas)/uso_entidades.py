#FORMAS DE IMPORTAR Y UTILIZAR MODULOS(BIBLIOTECAS):

#1
"""import entidad_operaciones

para usarlo de esta forma hay que escribir el nombre del paquete seguido de un . y el nombre de la funcion que se desea
entidad_operaciones.sumar(10,9)
entidad_operaciones.restar(10,9)
entidad_operaciones.multiplicar(4,4)


#2
from entidad_operaciones import sumar
solo permite usar las funciones importadas, en este caso sumar
sumar(10,9)


#3
from entidad_operaciones import *
agregando * permite usar todas las funciones del modulo importado