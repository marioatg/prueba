from io import open 
archivo=open("archivo.txt", "r")

archivo.seek(2)
print(archivo.read(6))