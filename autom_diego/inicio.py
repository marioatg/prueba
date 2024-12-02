import functools as fun
from io import open 
freq={}
archivo_texto=open('gaza.txt','r')

texto=archivo_texto.read()
lista_texto=texto.split(" ")
## Agarra lista, palabra y regresa el num de veces que ocurre 
## palabra en lista. 
## Marca error si palabra no está en lista. 
def f(lista,palabra): 
	y=filter(lambda x: x==palabra, lista)
	z=map(lambda x: 1, y)
	num=fun.reduce(lambda x,y: x+y,z)
	return(num)

def G(palabra):
	freq[palabra]=f(lista_texto,palabra)


for palabra in lista_texto:
	G(palabra)

total_palabras_diferentes= len(freq.keys())
valores_veces_palabras=freq.values()
lista_veces_palabras=list(valores_veces_palabras)
lista_veces_palabras.sort()
print(lista_veces_palabras)
for palabra, veces in freq.items():
	if veces == 6:
		print(palabra)
	else:
		continue


###---- no se usa
#palabras_distintas=list()
#for palabra in lista_ejemplo:
#	if palabra in palabras_distintas:
#		continue 
#	else:
#		palabras_distintas.append(palabra)

#print(len(palabras_distintas))
#lista4=[[lista_ejemplo]*4]

#a=map(f,[lista_ejemplo]*len(palabras_distintas),palabras_distintas)

#print(list(a))


