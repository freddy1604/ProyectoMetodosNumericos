import interes
import tkinter 

#Inicializacion de la ventana principal 
v0 = 100      # Depósito inicial
isem = 8/52      # Tasa de interés semanal (%)
n = 52        # Número de semanas
asem = 5      # Aporte semanal
final = interes.interes(v0,isem,n,asem)
#Devolver de decimal a hexadecimal el espectro RGB
def RGB_Hexadecimal (rojo:int, verde:int, azul:int): 
    colorRGB="#%02x%02x%02x" % (rojo, verde, azul)
    return colorRGB

#Ventana Principal del programa
ventana = tkinter.Tk() 
#Confirguracion del tamaño de la ventana
ventana.geometry("750x600")
ventana.config(background=RGB_Hexadecimal(255,250,250))
ventana.title("Caluculadora de Interes Compuesto") 

#Titulo para la Presentacion del programa 
titulo = tkinter.Label(ventana,text="Proyecto 1er Bimestre \n Métodos Numericos \n Integrantes \n Mijael Molina, Freddy Jimenez, David Pilataxi, Luis Lema",font=("Times New Roman",15,"bold"),relief="solid",background=RGB_Hexadecimal(0,255,255))

#Declaracion de todos los elementos que se utilizaran para el calculo y presentacion del interes compuesto
#Contenedor para los elementos de informacion
cont_Info = tkinter.Frame(ventana,relief="solid")

#Aporte interes
titulo_aporteInicial = tkinter.Label(cont_Info,text="Aporte inicial: ",font=("Arial",13))
entry_aporteInicial = tkinter.Entry(cont_Info) 
#Interes anual 
titulo_interesAnual = tkinter.Label(cont_Info,text="Interes anual: ",font=("Arial",13)) 
entry_interesAnual = tkinter.Entry(cont_Info)
porcentaje = tkinter.Label(cont_Info,text="%",font=("Arial",13))
#Aporte semanal 
titulo_aporteSem = tkinter.Label(cont_Info,text="Aporte Semanal",font=("Arial",13))
entry_aporteSem = tkinter.Entry(cont_Info)








#Colocacion del titulo y contenedor 
titulo.pack(pady=10,padx=15, fill=tkinter.X)
cont_Info.pack(pady=10,padx=15,fill=tkinter.BOTH)

#Colocacion de los elementos en el contendor
titulo_aporteInicial.grid(row=1,column=0,padx=20)
entry_aporteInicial.grid(row=1,column=1,padx=50)

titulo_interesAnual.grid(row=2,column=0,pady=20,padx=20)
entry_interesAnual.grid(row=2,column=1,pady=20,padx=50)
porcentaje.grid(row=2,column=2)

titulo_aporteSem.grid(row=3,column=0,padx=20)
entry_aporteSem.grid(row=3,column=1,padx=50)
ventana.mainloop() 
