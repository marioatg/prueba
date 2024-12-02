y=input("Introduzca numero:")

def f(x):
	return list(str(x))
print(f(y))
		
print("Programa para evaluar correos electrónicos.")
correo=list(input("Introduzca su dirección de correo electrónico: "))
valuacion=False
for i in correo: 
	if i=="@":
		lista2=correo[correo.index(i):]
for j in lista2:
	if j==".":
		valuacion=True

if valuacion==False:
	print("Nel")
else:
	print("Siu")	 		

