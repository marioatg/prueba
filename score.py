calif=input("Introduzca la calif: ")
def f(x):
	if float(x) >= 0.9:
		print("A")
	elif float(x) >= 0.8:
		print("B")
	elif float(x) >= 0.7:
		print("C")
	elif float(x) >= 0.6:
		print("D")
	elif float(x) < 0.6:
		print("F")
	else: 
		pass

try: 
	f(calif)
		
except: 
	print("No estes de pendeja.")
