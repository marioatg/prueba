import sqlite3
conexion=sqlite3.connect("base_ejemplo")
cursor=conexion.cursor()

#cursor.execute("INSERT INTO PRODUCTOS VALUES ('BARRA', 5000, 'HALTEROFILIA')")
#conexion.commit()
#datos=[("STRAPS",200,"HALTEROFILIA"), ("BALÓN",300,"FUTBOL")]
#cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", datos)
#conexion.commit()

cursor.execute("SELECT PRECIO,SECCION FROM PRODUCTOS")
output=cursor.fetchall()
print(output)
conexion.close()

col_edades=da['RIDAGEYR'].dropna()
lista_edades=[31]
col_edades.isin(lista_edades)

col_edades=da['RIDAGEYR'].dropna()
lista_edades=[31]
col_edades.isin(RIDAGEYR==31)



