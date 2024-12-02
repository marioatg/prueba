##Programa que calcula el n-esimo termino de la Fibnoacci.
n=int(input())
lista_fibo=[1,1]
if n==1 or n==2:
	print(1)
else:
	for i in range(n-2):
		nuevo_miembro=lista_fibo[-1] + lista_fibo[-2]
		lista_fibo.append(nuevo_miembro)
	print(nuevo_miembro)