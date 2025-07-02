def exibe_titulo():
    print("**************************************************")
    print("***** AGENDA TELEFÔNICA")
    print("**************************************************\n")

def exibe_opcoes_menu():
    print("1. vizualizar lista de contatos")
    print("6. sair")

def vizualizar_contatos(contatos):
    print("\nminha lista de contatos:")
    for index, contato in enumerate(contatos):
        index_ajustado = index + 1
        print(f"{index_ajustado}. {contato["Nome"]} | {contato["Telefone"]} | {contato["Email"]}")
    print()
    return

contatos = [{"Nome":"Rafael", "Telefone":"(11)99299-9483", "Email":"vansan.rafael@gmail.com" ,"Favorito":False},
            {"Nome":"Pam", "Telefone":"(11)98033-3796", "Email":"vansan.pam@gmail.com" ,"Favorito":False}]
while True:
    exibe_titulo()
    exibe_opcoes_menu()

    try:
        opcao = int(input("* escolha uma das opções do menu: "))
    except:
        print("opção inválida!")
    else:
        if opcao == 1:
            vizualizar_contatos(contatos)
        elif opcao == 6:
            break

