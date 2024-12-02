import pickle 
lista=["Lolo","1"]
lista_binaria=open("lista_binaria","wb")
pickle.dump(lista,lista_binaria)

lista_binaria.close()


lectura=open("lista_binaria","rb") #esto abre la info en binario en consola
lectura_entendible=pickle.load(lectura) #esto traduce a algo legible la info binaria

print(lectura_entendible)