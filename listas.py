lista1=["Alex","Paco","Pepe","Halo","Pan","cola"]
print(lista1[:])
print(lista1[2])
print(lista1[-1])
print(lista1[0:3])
print(lista1[1:3])
lista1.append(2)
print(lista1)
lista1.insert(0,"Teresforo")
print(lista1)
lista2=["bibol","rocky"]
lista1.extend(lista2)
print(lista1)
print(lista1.index("bibol"))

#### La funcion .index funciona con el minimo que aparezca 
### en la lista

print("Pepe" in lista1)
print("bibol" in lista2)

## .remove() es el dual de .insert()

lista2.remove("rocky")
print(lista2)
#El operador + funciona como union en las listas

lista3=lista1+lista2 
print(lista3[:])