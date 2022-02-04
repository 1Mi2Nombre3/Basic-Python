Lista1 = [1,2,3,4,5,6,7]
Lista2 = ['a','b','c','d','e','f']
Lista3 = ["Hola como estas"]
print("____________________")

print(Lista1)
print(Lista2)
print(Lista3)
print(Lista1[3])
print(Lista2[:3])
print(Lista3[3:])
print(Lista1[1:3])
print("____________________")

for i in range (1,3):
    print(Lista1[i])
print("____________________")
Lista11=[1,2,3,4,5,6,7,8,9,9,10]
print(Lista1)
Lista1.append(8)
Lista1.append(9)
Lista1.append(10)
print(Lista1)
Lista1.insert(1,9)     #inserta sobre un número ya defenido en la lista(posicion,cambio de variable)
print(Lista1)
Lista1.extend(Lista2)  #Une los elementos de una lista a otra lista ya defenida
print(Lista1)
Lista1.reverse()       #Invierte los elementos de una lista
print(Lista1)
print("_____________________")
for i in range(len(Lista1)-1,-1,-1):
    print(Lista1[i])
print("_____________________")
print(Lista11)
Lista11.pop(2)                  #Elimina un elemento de la lista en rango especifico
print(Lista11)
print("_____________________")
print(Lista11)
Lista11.remove(9)               #Elimina un elemento de la lista especificando el elemento
print(Lista11)
Lista11.pop()                   #Elimina
print("_____________________")
print(Lista11)
print(Lista11.index(7))
print(Lista11)
Lista11=[1,2,4,5,6,7]
print(sum(Lista11))
print(min(Lista11))
print(max(Lista11))
print("____________________")
cadena = "Hola como estas"
print(cadena[1])
print(cadena.split())
print(cadena)
listacadena = list(cadena)
print(listacadena)
print("____________________")
cadena2 = cadena.split()
print(cadena2)
delimitador = " "
cadena3 = delimitador.join(cadena2)  #Une cadenas separadas en una lista
print(cadena3)
print("____________________")
Lista8 = [1,2,3,4,5]
Lista9 = Lista8
print(Lista8,Lista9)
Lista8[2] = 10
print(Lista8,Lista9)
print("____________________")
Lista10 = Lista8.copy()              #Copia los elementos de una lista
print(Lista10)
Lista10[3]=11
print(Lista10,Lista8)
print("____________________")
Lista20 = [i*2 for i in range(5)]
print(Lista20)
Lista21 = [0,1,2,3,4]
print(Lista21[1]*2)
#diferente a
print(Lista21*2)
print("____________________")
s=0
a=3
b=4
for i in range(b):                  #Forma larga de una linea de (3*4)
    s=s+a
print(s)
print("____________________")
print(sum([a for i in range(b)]))    #Forma corta de una linea de (3*4)
print("____________________")



