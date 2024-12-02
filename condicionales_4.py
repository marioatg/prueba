dist_escuela=input("Que tan lejos vives de la escuela:")
print(dist_escuela)
num_hermanos=input("Cuantos hermanos tienes:")
print(num_hermanos)
salario_fam=input("Cuanto gana tu familia al mes:")
print(salario_fam)

if int(dist_escuela)>10 and int(num_hermanos)>2 and int(salario_fam)<=5000:
	print("Se te otorgará la beca.")
else:
	print("No se te otorgará la beca.")

print("Saludos.")		