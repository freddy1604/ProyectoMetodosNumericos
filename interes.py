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


    def valorFinal(self)->float: 
        termino1= self.v0*(1+(self.isem))**self.n
        subtermino2 = 0
        for i in range(0,self.n-1): 
            subtermino2 += (1+self.isem)**i 
            #print(subtermino2)
        return termino1+self.asem*subtermino2
    
    
v0 = 100      # Depósito inicial
isem = 8/52      # Tasa de interés semanal (%)
n = 52        # Número de semanas
asem = 5      # Aporte semanal
#intereses = interes(v0,isem,n,asem)
#print("El interes compuesto para el numero de semanas dado es: "+str(intereses.valorFinal())+"$")