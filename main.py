from operations import add, subtract, multiply, divide #Pega essas funções que estão no arquivo operations.py e traz pra cá

def show_menu(): #Uma função que apenas exibe o menu, não calcula nada, não retorna nada
    print("\n=== PYTHON CALCULATOR ===")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("0 - Exit")

def main(): # Função principal
    while True: # Loop infinito 
        show_menu()
        option = input("Choose an option: ")

        #Importante: input() sempre retorna string. Por isso se compara com "1" e não com 1.

        if option == "0":
            print("Closing calculator...")
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

if __name__ == "__main__": #Isso significa: "Só execute a função se este arquivo for executado diretamente"
    main() #Se alguém importar main.py em outro projeto: o código não roda automaticamente 