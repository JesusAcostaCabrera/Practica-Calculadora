'''
Aplicacion de calculadora
'''

import os

#Limpiar Consola
def Clear():
    input()
    os.system("cls")

#Asegurrase de que quiere salir
def End():
    repeat = ""
    while repeat != "yes" and repeat != "no":
            print("¿Do you want to use another function?\n")
            print("Please answer yes or no")

            print("Your answer is: ",end="")
            repeat = input()
            repeat = repeat.lower()
            match repeat:
                case "yes":
                    return True
                case "no":
                    return False
                case _:
                    print("Please, write yes or no")
                    Clear()

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

#Variable Global

if __name__ == '__main__':

    run = bool(True)
    while run is True:
        os.system("cls")
        option = -1

        while option < 1 or option > 4:
            print("Hello, this program will serve as a simple calculator.\n Please, choose an option.")
            print("1. Sum               2. Substraction\n3.Multiplication     4. Division\n\n")

            print("Your Option is: ", end ="")
            option = int(input())
            if option < 1 or option > 4:
                print("You didn't choose a number between 1 and 4")
                Clear()
        
            
            Opt = Operations(int(input("First Number: ")), int(input("Second Number: ")))

            print(Opt.num1)
            
            print("The result is:", end=" ")

            match option:
                case 1:
                    print(Opt.Sum())
                case 2:
                    print(Opt.Sub())
                case 3:
                    print(Opt.Mult())
                case 4:
                    print(Opt.Div())
        
            print("Press enter to continue.\n\n", end="")
            input()
            os.system("cls")

            run = End()                    
        