import interes
import tkinter 

#Inicializacion de la ventana principal 
v0 = 100      # Depósito inicial
isem = 8/52      # Tasa de interés semanal (%)
n = 52        # Número de semanas
asem = 5      # Aporte semanal
final = interes.interes()


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
cont_Info = tkinter.Frame(ventana)

#Aporte interes
titulo_aporteInicial = tkinter.Label(cont_Info,text="Aporte inicial: ",font=("Arial",13))
entry_aporteInicial = tkinter.Entry(cont_Info) 
#Interes anual 
titulo_interesAnual = tkinter.Label(cont_Info,text="In")

#Colocacion del titulo y contenedor 
titulo.pack(pady=10,fill=tkinter.X)
cont_Info.pack(pady=10,padx=15,fill=tkinter.BOTH)

#Colocacion de los elementos en el contendor
titulo_aporteInicial.grid(row=1,column=0)
entry_aporteInicial.grid(row=1,column=1,padx=50)


#asd

# Variables para los radio buttons
frecuencia_variable = tkinter.StringVar(value="")

# Título para los radio buttons
titulo_frecuencia = tkinter.Label(ventana, text="Frecuencia:", font=("Arial", 13), bg=RGB_Hexadecimal(255, 250, 250))
titulo_frecuencia.pack(padx=100, pady=10)

# Frame para organizar los radio buttons en fila
frame_frecuencia = tkinter.Frame(ventana, bg=RGB_Hexadecimal(255, 250, 250))
frame_frecuencia.pack(pady=5)

# Crear los radio buttons con bordes y color personalizable
opciones = [("Semanal", "semanal"), ("Mensual", "mensual"), ("Trimestral", "trimestral"), ("Bimestral", "bimestral")]

for texto, valor in opciones:
    tkinter.Radiobutton(
        frame_frecuencia, 
        text=texto, 
        value=valor, 
        variable=frecuencia_variable, 
        font=("Arial", 12), 
        bg=RGB_Hexadecimal(255, 250, 250), 
        relief="solid", 
        bd=1,  # Borde del recuadro
        highlightbackground=RGB_Hexadecimal(192, 192, 192),  # Color del borde
        highlightthickness=1  # Grosor del borde
    ).pack(side="right", padx=40, pady=5)


ventana.mainloop()