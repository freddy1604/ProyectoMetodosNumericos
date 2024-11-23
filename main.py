import tkinter.messagebox
import interes
import tkinter 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



#Devolver de decimal a hexadecimal el espectro RGB
def RGB_Hexadecimal (rojo:int, verde:int, azul:int): 
    colorRGB="#%02x%02x%02x" % (rojo, verde, azul)
    return colorRGB

#Calcular el interes compuesto recopilando todos los datos:
def CalculoInteresCompuesto():
    try:
        v0= float(entry_aporteInicial.get())
        frecuenciaSeleccionada = frecuencia_variable.get()
        ianual = float(entry_interesAnual.get())

        if frecuenciaSeleccionada=="":
            ianual = ianual/12
        else:
            ianual = ianual/int(frecuenciaSeleccionada)
        
        n = int(entry_NumeroPeriodosTranscurridos.get())
        asem = float(entry_aporteSem.get())
        interes_compuesto = interes.interes(v0,ianual,n,asem)
        valor_final = interes_compuesto.valorFinal(n)
        resultado_final.configure(text=str(round(valor_final,4)))
        interes_compuesto.grafica()
        ventana.update_idletasks()
    except Exception as e:
        tkinter.messagebox.showerror("Error","Error al ingresar los datos:\n"+str(e))




#Inicializacion de la ventana principal 
#Ventana Principal del programa
ventana = tkinter.Tk() 
#Confirguracion del tamaño de la ventana
ventana.geometry("900x750")
ventana.config(background=RGB_Hexadecimal(255,250,250))
ventana.title("Caluculadora de Interes Compuesto") 

#Titulo para la Presentacion del programa 
titulo = tkinter.Label(ventana,text="Proyecto 1er Bimestre \n Métodos Numericos \n Integrantes \n Mijael Molina, Freddy Jimenez, David Pilataxi, Luis Lema",font=("Times New Roman",15,"bold"),relief="solid",background=RGB_Hexadecimal(0,255,255))

#Declaracion de todos los elementos que se utilizaran para el calculo y presentacion del interes compuesto
#Contenedor para los elementos de informacion

cont_Info = tkinter.Frame(ventana)
cont_Info = tkinter.Frame(ventana,relief="solid")

#Aporte interes
titulo_aporteInicial = tkinter.Label(cont_Info,text="Aporte inicial: ",font=("Arial",13))
entry_aporteInicial = tkinter.Entry(cont_Info) 
#Interes anual 
titulo_interesAnual = tkinter.Label(cont_Info,text="Interes anual",font=("Arial",13))
entry_interesAnual = tkinter.Entry(cont_Info)
porcentaje = tkinter.Label(cont_Info,text="%",font=("Arial",13))
#Aporte semanal 
titulo_aporteSem = tkinter.Label(cont_Info,text="Aporte Semanal",font=("Arial",13))
entry_aporteSem = tkinter.Entry(cont_Info)

#Colocacion del titulo y contenedor 
titulo.pack(pady=10,fill=tkinter.X)
cont_Info.pack(pady=10,padx=15,fill=tkinter.BOTH)



# Crear los radio buttons con bordes y color personalizable
opciones = [("Semanal", 52), ("Mensual", 12), ("Trimestral", 4), ("Bimestral", 6)]

# Variables para los radio buttons
frecuencia_variable = tkinter.StringVar(value=" ")

# Título para los radio buttons
titulo_frecuencia = tkinter.Label(cont_Info, text="Periodo:", font=("Arial", 13))



#Colocacion del titulo y contenedor 
titulo.pack(pady=10,padx=15, fill=tkinter.X)
cont_Info.pack(pady=10,padx=15,fill=tkinter.BOTH)

#Colocacion de los elementos en el contendor
titulo_aporteInicial.grid(row=1,column=0,padx=20)
entry_aporteInicial.grid(row=1,column=1,padx=50)

titulo_interesAnual.grid(row=2,column=0,pady=20,padx=20)
entry_interesAnual.grid(row=2,column=1,pady=20,padx=50)
porcentaje.grid(row=2,column=1,columnspan=2)

titulo_aporteSem.grid(row=3,column=0,padx=20)
entry_aporteSem.grid(row=3,column=1,padx=50)

titulo_frecuencia.grid(row=4,column=0,pady=10,padx=70)
i=0
for texto, valor in opciones:
    tkinter.Radiobutton(
        cont_Info, 
        text=texto, 
        value=valor, 
        variable=frecuencia_variable, 
        font=("Arial", 12), 
        bg=RGB_Hexadecimal(255, 250, 250), 
        relief="solid", 
        bd=1,  # Borde del recuadro
        highlightbackground=RGB_Hexadecimal(192, 192, 192),  # Color del borde
        highlightthickness=1  # Grosor del borde
    ).grid(row=5,column=i, padx=40, pady=5)
    i+=1


#Número de periodos transcurridos
titulo_NumeroPeriodosTranscurridos = tkinter.Label(cont_Info, text="Número de Periodos Transcurridos:", font=("Arial", 13))
titulo_NumeroPeriodosTranscurridos.grid(row=6,pady=20,column =0)
entry_NumeroPeriodosTranscurridos = tkinter.Entry(cont_Info) 
entry_NumeroPeriodosTranscurridos.grid(row=6, column = 1, padx=50)


# Botón Calcular 
boton_calcular = tkinter.Button(cont_Info, text="Calcular", font=("Arial", 13, "bold"), bg=RGB_Hexadecimal(0, 255, 127), relief="raised", command=CalculoInteresCompuesto)
boton_calcular.grid(row=7, column=0, columnspan=4, pady=10)

#Valor final
valorfinal = tkinter.Label(cont_Info, text="Valor Final", font=("Arial", 15, "bold"))
valorfinal.grid(row=8,column=1, pady= 10)

#Label resultado final
resultado_final = tkinter.Label(cont_Info, text="", font=("Arial", 16))
dinero = tkinter.Label(cont_Info,text="$",font=("Arial", 16,"bold"))
resultado_final.grid(row=9,column=1, pady= 10)
dinero.grid(row=9,column=3)

# Obtener dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Dimensiones de la ventana
ancho_ventana = 900
alto_ventana = 750

# Coordenadas para centrar la ventana y moverla ligeramente hacia arriba
x = int((ancho_pantalla / 2) - (ancho_ventana / 2))
y = int((alto_pantalla / 2) - (alto_ventana / 2)) - 50  # Mover 50 píxeles hacia arriba

# Configurar posición y tamaño de la ventana
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
ventana.config(background=RGB_Hexadecimal(255, 250, 250))
ventana.title("Calculadora de Interés Compuesto")


ventana.mainloop() 

