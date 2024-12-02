number=int(input("Enter the number you wanna know about:"))
if  number%2==1:
    print("Weird")
elif number%2==0 and number in [2,3,4,5]:
    print("Not Weird")
elif number%2==0 and 6 <= number <=20:
    print("Weird") 
elif number%2==0 and 20 < number:
    print("Not Weird")         
