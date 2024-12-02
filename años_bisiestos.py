ano=int(input("Introduzca el año: "))

def is_leap(year):
    leap = False
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap = True 
            else: 
                leap = False    
        else: 
            leap = True    
    else:      
        leap = False  
    return leap     
print(is_leap(ano))       

lista=[]
for i in range(5):
    lista=lista+[i]
print(lista)

    

