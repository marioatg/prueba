archivo=open('prueba.txt')
list_correos = list()
for line in archivo:
	if len(line.split()) <2: 
		continue
	else: 
		list_line=line.split()
		if list_line[0]=='From':
			list_correos.append(list_line[1])
		else:
			pass
for correo in list_correos:
	print(correo)
	count=count +1 


