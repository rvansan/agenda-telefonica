def exibe_titulo():
    print("**************************************************")
    print("***** AGENDA TELEFÔNICA")
    print("**************************************************\n")
    return

def exibe_opcoes_menu():
    print("1. adicionar contato")
    print("2. vizualizar lista de contatos")
    print("3. editar contato")
    print("4. marcar/ desmarcar como favorito")
    print("5. exibir lista de contatos favoritos")
    print("6. sair")
    return

def adicionar_contato(contatos):
    nome = input("digite o nome do novo contato: ")
    telefone = input("digite o telefone do novo contato: ")
    email = input("digite o email do novo contato: ")
    contato = {"Nome": nome, "Telefone": telefone, "Email": email ,"Favorito":False}
    contatos.append(contato)
    vizualizar_contatos(contatos)
    return

def vizualizar_contatos(contatos):
    print("\nminha lista de contatos:")
    for index, contato in enumerate(contatos):
        index_ajustado = index + 1
        favorito = " | Favorito" if contato["Favorito"] else ""
        print(f"{index_ajustado}. {contato["Nome"]} | {contato["Telefone"]} | {contato["Email"]} {favorito}")
    print()
    return

def editar_contato(contatos):
    vizualizar_contatos(contatos)
    while True:
        try:
            index_contato_editar = int(input("digite a chave do contato que deseja editar: "))
            index_ajustada = index_contato_editar - 1
            contato = contatos[index_ajustada]
        except:
            print("chave inválida!")
        else:
            contatos[index_ajustada]["Nome"] = input("digite o novo nome do novo: ")
            contatos[index_ajustada]["Telefone"] = input("digite o novo telefone do novo: ")
            contatos[index_ajustada]["Email"] = input("digite o novo email do novo: ")
            vizualizar_contatos(contatos)
            break
    return

def marcar_desmarcar_favorito(contatos):
    vizualizar_contatos(contatos)
    while True:
        try:
            index_contato_editar = int(input("digite a chave do contato que deseja marcar/ desmarcar como favorito: "))
            index_ajustada = index_contato_editar - 1
            contato = contatos[index_ajustada]
        except:
            print("chave inválida!")
        else:
            contatos[index_ajustada]["Favorito"] = not contatos[index_ajustada]["Favorito"]
            vizualizar_contatos(contatos)
            break
    return

def exibir_favoritos(contatos):
    print("\nminha lista de contatos favoritos:")
    for index, contato in enumerate(contatos):
        if contato["Favorito"]:
            index_ajustado = index + 1
            favorito = " | Favorito" if contato["Favorito"] else ""
            print(f"{index_ajustado}. {contato["Nome"]} | {contato["Telefone"]} | {contato["Email"]} {favorito}")
    print()
    return


contatos = [{"Nome":"Contato 1", "Telefone":"(11)99999-9999", "Email":"contato1@email.com" ,"Favorito":False},
            {"Nome":"Contato 2", "Telefone":"(11)88888-8888", "Email":"contato2@email.com" ,"Favorito":True},
            {"Nome":"Contato 3", "Telefone":"(11)77777-7777", "Email":"contato3@email.com" ,"Favorito":False}]

while True:
    exibe_titulo()
    exibe_opcoes_menu()

    try:
        opcao = int(input("* escolha uma das opções do menu: "))
    except:
        print("opção inválida!")
    else:
        if opcao == 1:
            adicionar_contato(contatos)
        elif opcao == 2:
            vizualizar_contatos(contatos)
        elif opcao == 3:
            editar_contato(contatos)
        elif opcao == 4:
            marcar_desmarcar_favorito(contatos)
        elif opcao == 5:
            exibir_favoritos(contatos)
        elif opcao == 6:
            break

