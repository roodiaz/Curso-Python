'''
#serializacion consiste en guardar en un fichero ext una coleccion, dicc u objt,
#se guarda codificado en codigo bin
#es necesaria la biblioteca Pickle para usar los metodos:

  dump(): volcado de datos al fichero binario externo
  load(): carga de datos del fichero binario externo   

'''
import pickle
from io import open

#guardar en bin:
lista_nombres=["pedro","ana","maria","lucas"]
save_fichero=open("lista_nombres","wb")
pickle.dump(lista_nombres,save_fichero)
#primer param datos a guardar, segundo param donde guardar los datos

save_fichero.close()


#leer archivos bin:
open_fichero=open("lista_nombres","rb")
lista=pickle.load(open_fichero)
print(lista)




