# Inicialização de variáveis de estado
opcao_menu = ""

while opcao_menu != "2":
    # Exibição do Menu Principal
    print("-" * 30)
    print(f"{'MENU INICIAL':^30}")
    print("-" * 30)
    print("1. Iniciar Novo Jogo")
    print("2. Sair do Programa")
    print("-" * 30)
    
    opcao_menu = input("Escolha uma opção: ")

    if opcao_menu == "1":
        # Reset de pontuação para uma nova rodada
        pontos_totais = 0
        
        print("\n--- INICIANDO QUIZ ---")
        print("Responda com o número da opção correta.\n")

        # Pergunta 1
        print("1) Quando foi a Independência do Brasil?")
        print("1. 1834")
        print("2. 1827")
        print("3. 1822")
        print("4. 1819")
        resposta = input("Sua resposta: ")
        
        if resposta == "3":
            print("Correto! +10 pontos.")
            pontos_totais = pontos_totais + 10
        else:
            print("Errou! O correto seria a opção 3 (C).")

        # Pergunta 2
        print("\n2) Qual o sinônimo de guarita?")
        print("1. Veneta")
        print("2. Vedeta")
        print("3. Vendeta")
        resposta = input("Sua resposta: ")

        if resposta == "2":
            print("Correto! +10 pontos.")
            pontos_totais = pontos_totais + 10
        else:
            print("Errado. A resposta correta era a opção 2 (Ada Lovelace).")

        # Pergunta 3
        print("\n3) O que significa a sigla SQL?")
        print("1. Simple Query Language")
        print("2. System Quick Logic")
        print("3. Structured Query Language")
        resposta = input("Sua resposta: ")

        if resposta == "3":
            print("Correto! +10 pontos.")
            pontos_totais = pontos_totais + 10
        else:
            print("Errado. A resposta correta era a opção 3 (Structured Query Language).")

        # Cálculo da Classificação Final
        classificacao = ""
        if pontos_totais == 0:
            classificacao = "Estagiário"
        elif pontos_totais <= 10:
            classificacao = "Iniciante"
        elif pontos_totais <= 20:
            classificacao = "Conhecedor"
        else:
            classificacao = "Mestre da Computação"

        # Exibição dos resultados com f-string
        print("\n" + "="*30)
        print(f"RESULTADO FINAL")
        print(f"Pontuação Total: {pontos_totais} pontos")
        print(f"Sua Classificação: {classificacao}")
        print("="*30 + "\n")

    elif opcao_menu == "2":
        print("Encerrando o sistema... Até logo!")
    
    else:
        print("\n[ERRO] Opção inválida! Tente novamente.\n")

print("Programa finalizado com sucesso.")