#Estas tres primeras lineas crean una ventana.
from tkinter import *
raiz = Tk()
raiz.title('Programa0')
#Este nos permite cambiar el tamaño de la ventana
#en ancho y alto. 
raiz.resizable(True,True)
## config permite cambiar el color del background de la ventana. 
raiz.config(bg='yellow')
##geometry permite cambiar el tamaño de la raíz.
#raiz.geometry('600x600')
## Creando un frame: 
miFrame=Frame()
##Empaquetandolo en la raíz
miFrame.pack()
##dandole color
miFrame.config(bg='red')
miFrame.config(width='400',height='400')
#Si se quiere que no se abra la consola al ejecutar este 
#programa, hay que guardarlo como .pyw o ejecutarlo como pythonw.exe
#Esta linea hace que la ventana este en ejecucion siempre.
# mainloop siempre debe estar al final
raiz.mainloop()