print("programa para calcular maximo")
x=int(input("Introduzca el numero 1: "))
y=int(input("Introduzca el numero 2: "))


def devuelvemax(num1,num2):
	if num1<num2: 
		return num2
	else: 
		return num1	 

print(devuelvemax(x,y))
