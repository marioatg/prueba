def ciudades_de_paises(*paises):
	for pais in paises:
		yield from pais 
Mexico=["DF","Guadalajara"] 
Colombia=["Cali", "Medellín"]
arreglo=ciudades_de_paises(Mexico,Colombia)

print(next(arreglo))

print(next(arreglo))
print(next(arreglo))
print(next(arreglo))

#Este comando lo que hace es acceder a los elementos de elementos de una tupla. 




