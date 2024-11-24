import matplotlib.pyplot as plt
import numpy as np
class interes: 
    # v0 = Valor del deposito inicial 
    # isem = Tasa de interes semanal en porcentaje
    # n = Numero de periodos transcurridos
    # asem = Aportes semanales 

    def __init__(self,v0:float,isem:float,n:int,asem:float):
        self.v0 = v0
        self.isem = isem/100
        self.n = n
        self.asem = asem


    def valorFinal(self,periodos)->float: 
        termino1= self.v0*(1+(self.isem))**periodos
        subtermino2 = 0
        for i in range(0,periodos-1): 
            subtermino2 += (1+self.isem)**i 
            #print(subtermino2)
        return termino1+self.asem*subtermino2
    
    def grafica(self):
        fig,ax = plt.subplots()
        periodos = np.arange(0,self.n) 
        valores = [self.valorFinal(p) for p in periodos]
        ax.plot(periodos,valores,label="Valor final")
        ax.set_xlabel("Periodos")
        ax.set_ylabel("Ahorro $")
        ax.set_title("Evolución del Ahorro")
        ax.legend()
        ax.grid()
        fig.show()




    
v0 = 100      # Depósito inicial
isem = 8/52      # Tasa de interés semanal (%)
n = 52        # Número de semanas
asem = 5      # Aporte semanal
#intereses = interes(v0,isem,n,asem)
#print("El interes compuesto para el numero de semanas dado es: "+str(intereses.valorFinal())+"$")