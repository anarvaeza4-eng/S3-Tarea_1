class NumeroPrimo:
    # atributo de clase o estatico
    # este valor s emantiene par atodas las instancias
    primos_verficados=[]
    def __init__(self):
        # atributo de instancia
        # este valor se mantiene para cada objeto creado de la clase
        self.historial=[]

    def es_primo(self,numero):
        self.historial.append(numero)
        primo=True
        if numero < 2:
            primo=False
        else:
            for i in range(2,numero):#(2,3,4..)
                if numero % i == 0:
                    primo=False
                    break

        #if primo:NumeroPrimo.primos_verficados.append(numero) 
        return primo


    def primos_en_rango(self,*args):
        primos=[]
        
        for num in args:
            
            if self.es_primo(num)==True:
                primos.append(num)
                NumeroPrimo.primos_verficados.append(num)
                
      
        return primos        

    def cantidad_verificados(self):
        return len(self.historial)

    @staticmethod # accesa a los atributos de clase o estatico
    def get_primos_verificados():
        return len(NumeroPrimo.primos_verficados)
     
# instancia la clase y crea un objeto primo1(variable)   
primo1 = NumeroPrimo()
# para llamar a atirbutos y metodos de la clase se usa el operador punto (.)
# prueba el método es_primo con el número 7
if primo1.es_primo(2):
    print("El número es primo")
    NumeroPrimo.primos_verficados.append(2)
else:
    print("El número 2, no es primo")

print(primo1.primos_en_rango(9,3))
print(primo1.historial)
print(primo1.cantidad_verificados())

primo2=NumeroPrimo()
if primo1.es_primo(5):
    print("El número es primo")
    NumeroPrimo.primos_verficados.append(5)
else:
    print("El número 5, no es primo")

print(primo2.historial)
print(NumeroPrimo.primos_verficados)
print(NumeroPrimo.get_primos_verificados())