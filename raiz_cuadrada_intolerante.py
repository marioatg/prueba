import math 

numero=int(input("Numero: "))
intentos=0

while numero <0:
	print("la estas cagando, usa positivos")
	intentos=intentos+1
	print("Llevas " + str(intentos)+ "intento(s)")

	numero=int(input("Numero: "))

	if intentos >3:
		break; 

if intentos<=4:
	raiz=math.sqrt(numero)
	print(raiz)
else:
	print("Ya mamaste")



