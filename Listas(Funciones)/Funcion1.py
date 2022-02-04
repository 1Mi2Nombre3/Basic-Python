#añadir un dato a una lista pero (al final).
lista=[1,2,3]
lista.append(15)
print(lista)

#añadir un dato a una lista donde queremos.
lista.insert(0,20)   #2valores el primero es la posicion y el segundo lo que quiero agregar
print(lista)

#Remover un valor a la lista sin devolver el valor.
lista.remove(2)   #Eliminar un valor de la lista
print(lista)

#Remueve un valor de una posicion y se lo pasa a otra variable
valor=lista.pop(0)
print("Soy valor",valor)
print(lista)

#Elima toudo de una lista
lista.clear()
print(lista)

#Cuenta los repetidos de una lista (srive para remover despues)
lista=[1,2,2,2,2,3,4,5,6,7]
cantidad=lista.count(2)         #cuenta cuantas veces se repite cierta variable en ()
print(cantidad)

#Unir 2 listas en 1 sola.
lista2=["developer","pe","Hola"]
lista.extend(lista2)
print(lista)

#Copiar una lista a otra sin nodificar a otra lista
lista2=lista.copy()
print(lista2)


































