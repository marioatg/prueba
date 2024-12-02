tupla1=(2,3,4,5,3,3,3,3,3)
tupla2=("Erick","Bombin",117)
lista1=list(tupla1)
print("Bombin" in lista1)
print(3 in lista1)
print(tupla1.count(3))
tupla3=tuple(lista1)
print(tupla3.count(3))
#Para tuplas con un unicoelemento
#se tiene que finalizar con una coma
tupla4=(1,1,1,1,1)
print(len(tupla4))
tupla5=("ano",)
print(len(tupla5))
#las tuplas se pueden escribir sin sus parentesis
#se pueden extraer datos de tupla hacia variables 
#distintas 
tupla6=(2,117,"Juan",2.14,160)
generacion, numero, nombre, altura, peso=tupla6
print(peso)
