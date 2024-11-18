import interes
import tkinter 

#Inicializacion de la ventana principal 
v0 = 100      # Depósito inicial
isem = 8/52      # Tasa de interés semanal (%)
n = 52        # Número de semanas
asem = 5      # Aporte semanal
final = interes.interes(v0,isem,n,asem)
ventana = tkinter.Tk() 
ventana.geometry("750x600")
ventana.title("Caluculadora de Interes Compuesto")
titulo = tkinter.Label(ventana,text="Proyecto 1er Bimestre \n Métodos Numericos",)
titulo_interes = tkinter.Label(ventana,text="Interes anual")
dato_interes = tkinter.Entry(ventana)
titulo.pack(pady=10)
titulo_interes.pack(pady=10)
dato_interes.pack(pady=10)
valorFinal = tkinter.Label(ventana,text="El interes final es:"+str(final.valorFinal()))
valorFinal.pack(pady=10)
ventana.mainloop()