######## Entorno de pruebas. 
import re 
archivo = open('archivo.txt','r')
for line in archivo:
	if re.search('^Stalin', line):
		print(line)