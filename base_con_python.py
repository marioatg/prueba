import sqlite3
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')
conn.close()

conexion = sqlite3.connect(path)

cursor=conexion.cursor()

### Ejercicio 8.4
fh=open(fname,'r')
text = fh.read()
lista_definitiva=list()
for line in texto_prueba.split('\n'):
	lista_palabras_en_linea=line.split()
	for palabra in lista_palabras_en_linea:
		if palabra in lista_definitiva:
			pass 
		else:
			lista_definitiva.append(palabra)
print(lista_definitiva)




