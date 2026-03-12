from operations import add, subtract, multiply, divide #Pega essas funções que estão no arquivo operations.py e traz pra cá
from math_game import jogar, gerar_pergunta

def calculator_menu(): #Uma função que apenas exibe o menu, não calcula nada, não retorna nada
    print("\n=== PYTHON CALCULATOR ===")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("0 - Back")

def calculator():
    while True: # Loop infinito 
        calculator_menu()
        option = input("Choose an option: ")

        #Importante: input() sempre retorna string. Por isso se compara com "1" e não com 1.

        if option == "0":
            break # O programa só para quando encontra um break

        if option in ["1", "2", "3", "4"]: #Verificação de opções válidas
            try: #Tratamento de erro
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if option == "1":
                    result = add(num1, num2)
                elif option == "2":
                    result = subtract(num1, num2)
                elif option == "3":
                    result = multiply(num1, num2)
                elif option == "4":
                    result = divide(num1, num2)
                
                print(f"Result: {result}")

            except ValueError: #Tratamento de erro numérico
                print("Erro: Please enter valid numbers.")

        else:
            print("Invalid option. Plese try again.")