print("verificacion de edad")
edad_usuario=int(input("Introduzca su edad:"))
#No puede haber un else sin su correspondiente
#if
if edad_usuario < 18:
	print("No estás autorizado a entrar al sitio")
else: 
	print("Puedes pasar")

print("función característica de los positivos")

valor=int(input("Introduzca un número:"))

def c(x):
	y=1
	if x >0:
		return y 
	else: 
		return y -1 
				
print(c(valor))	