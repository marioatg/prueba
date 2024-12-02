interseccion=["elemento_invisible"]
numero=input("Numero:")
for i in list(numero):
	if i=="0" or i=="4" or i=="6" or i=="8" or i=="9":
		interseccion=interseccion+[i]
	else:
		interseccion=interseccion


y=0
for i in range(len(interseccion)-1):
	y=y+1
	
print(y)




