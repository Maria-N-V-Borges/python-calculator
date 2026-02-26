from operations import add, subtract, multiply, divide #Pega essas funções que estão no arquivo operations.py e traz pra cá

def mostrar_menu(): #Uma função que apenas exibe o menu, não calcula nada, não retorna nada
    print("\n=== CALCULADORA PYTHON ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

def main(): # Função principal
    while True: # Loop infinito 
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        #Importante: input() sempre retorna string. Por isso se compara com "1" e não com 1.

        if opcao == "0":
            print("Encerrando a calculadora...")
            break # O programa só para quando encontra um break

        if opcao in ["1", "2", "3", "4"]: #Verificação de opções válidas
            try: #Tratamento de erro
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if opcao == "1":
                    resultado = add(num1, num2)
                elif opcao == "2":
                    resultado = subtract(num1, num2)
                elif opcao == "3":
                    resultado = multiply(num1, num2)
                elif opcao == "4":
                    resultado = divide(num1, num2)
                
                print(f"Resultado: {resultado}")

            except ValueError: #Tratamento de erro numérico
                print("Erro: Digite apenas números válidos.")

        else:
            print("Opção inválido. Tente novamente.")

if __name__ == "__main__": #Isso significa: "Só execute a função se este arquivo for executado diretamente"
    main() #Se alguém importar main.py em outro projeto: o código não roda automaticamente 