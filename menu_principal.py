import runpy

def menu():
    while True:
        print("\n=== MENU DE OPÇÕES ===")
        print("1 - Converter metros para centímetros")
        print("2 - Calcular a área de um círculo")
        print("3 - Calcular a área de um quadrado")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            runpy.run_path("5.py")
            return True  # indica que o programa deve continuar
        elif opcao == "2":
            runpy.run_path("6.py")
            return True
        elif opcao == "3":
            runpy.run_path("7.py")
            return True
        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            return False  # indica que o programa deve parar
        else:
            print("Opção inválida! Tente novamente.")

# Loop principal
while True:
    continuar = menu()
    if not continuar:
        break

    resposta = input('\nDeseja voltar ao menu? (S/N): ').strip().lower()
    if resposta != "s":
        print('\nObrigado! Até a próxima!')
        break
