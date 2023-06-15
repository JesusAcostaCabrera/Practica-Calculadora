'''
Aplicacion de calculadora
'''
import os
import random
import Opt

#Limpiar Consola
def Clear():
    input()
    os.system("cls")

#Asegurrase de que quiere salir
def End():
    repeat = ""
    while repeat in ("yes", "no"):
            print("¿Do you want to use another function?\n")
            print("Please answer yes or no")

            print("Your answer is: ",end="")
            try:
                repeat = input()
                repeat = repeat.lower()
            except:
                repeat = "yes" if random.randint(1,2) == 1 else "no"
                
            match repeat:
                case "yes":
                    return True
                case "no":
                    return False
                case _:
                    print("Please, write yes or no")
                    Clear()

#Variable Global

if __name__ == "__main__":

    run = bool(True)
    while run is True:
        os.system("cls")
        option = -1

        while option < 1 or option > 4:
            print("Hello, this program will serve as a simple calculator.\n Please, choose an option.")
            print("1. Sum               2. Substraction\n3.Multiplication     4. Division\n\n")

            print("Your Option is: ", end ="")
            try:
                option = int(input())
                if option < 1 or option > 4:
                    print("You didn't choose a number between 1 and 4")
                    Clear()
                Op = Opt.Operations(int(input("First Number: ")), int(input("Second Number: ")))
            except:
                option = random.randint(1,4)
                Op = Opt.Operations(random.randint(1,9),random.randint(1,9))

            
            print("The result is:", end=" ")

            match option:
                case 1:
                    print(Op.Sum())
                case 2:
                    print(Op.Sub())
                case 3:
                    print(Op.Mult())
                case 4:
                    print(Op.Div())

            try:
                print("Press enter to continue.\n\n", end="")
                input()
            except:
                print()                

            os.system("cls")

            run = End()                    
        