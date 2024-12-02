import __future__

numero=int(input())

lista=[]
for i in range(numero):
    lista=lista+[i+1]
print(*lista, sep='', end='\n',)
    