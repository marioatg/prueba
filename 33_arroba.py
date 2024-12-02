##Programa para calcular la paga de un empleado tomando en cuenta que a partir de 30 horas laboradas se paga el 25 por ciento extra.
numero_de_horas=input("Ingrese las horas laboradas en esta semana:")
try:
	if int(numero_de_horas)<=48:
		print("Su pago es " + str(int(numero_de_horas)*50))
	else:
		print("Su pago es " + str(int(numero_de_horas)*(50*1.25)))
except:
	print("Por favor, introduce un numero.")

lista = [1,2]

