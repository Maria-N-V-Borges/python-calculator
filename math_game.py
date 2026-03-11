import random

def gerar_pergunta(nivel):
    """
    Gera dois números aleatórios com base no nível e retorna a pergunta e a resposta.
    """
    if nivel == "easy":
        num1 = random.randint(1, 5)
        num2 = random.randint(1, 5)
    else:  # nivel hard
        num1 = random.randint(6, 9)
        num2 = random.randint(6, 9)
    
    resposta_correta = num1 * num2
    pergunta = f"Quanto é {num1} x {num2}? "
    
    return pergunta, resposta_correta

def jogar():
    print("--- Desafio de Multiplicação ---")
    escolha = input("Escolha o nível (1 para Easy, 2 para Hard): ")
    
    nivel = "easy" if escolha == "1" else "hard"
    
    # Gera a pergunta e a resposta correta
    texto_pergunta, correta = gerar_pergunta(nivel)
    
    # Sistema de entrada do usuário
    try:
        tentativa = int(input(texto_pergunta))
        
        # Verificação
        if tentativa == correta:
            print("✅ Parabéns! Você acertou.")
        else:
            print(f"❌ Errou! O resultado correto era {correta}.")
    except ValueError:
        print("Por favor, digite apenas números inteiros!")

# Iniciar o jogo
if __name__ == "__main__":
    jogar()
