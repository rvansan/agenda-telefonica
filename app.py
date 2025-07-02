def exibe_titulo():
    print("**************************************************")
    print("***** AGENDA TELEFÔNICA")
    print("**************************************************\n")

def exibe_opcoes_menu():
    print("6. sair")

while True:
    exibe_titulo()
    exibe_opcoes_menu()

    try:
        opcao = int(input("* escolha uma das opções do menu: "))
    except:
        print("opção inválida!")
    else:
        if opcao == 6:
            break