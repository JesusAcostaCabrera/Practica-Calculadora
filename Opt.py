#Clase con todas las operaciones aritmeticas
class Operations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    #Suma
    def Sum(self):
        return (self.num1)+(self.num2)
    
    #Resta
    def Sub(self):
        return self.num1-self.num2
    
    #Multiplicacion
    def Mult(self):
        return self.num1*self.num2
    
    #Division
    def Div(self):
        return self.num1/self.num2
