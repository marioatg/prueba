print("Programa para calcular la media aritmetica de 3 numeros.")
num1=int(input("Introduzca el primero: "))
num2=int(input("Introduzca el segundo: "))
num3=int(input("Introduzca el tercero: "))

def media(x,y,z): 
	a=x+y+z
	return a/3
print(media(num1,num2,num3))	