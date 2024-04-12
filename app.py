import os


def sair():
    os.system("cls")
    print("Finalizando aplicação.\n")


def opcao_invalida():
    print("Opção Inválida\n")
    input("Digite qualquer tecla para retornar ao menu: ")
    main()


def chama_nome_app():
    print("Programa Expresso")


def exibir_opcoes():
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar restaurante")
    print("4 - Sair\n")


def escolha_opcoes():
    try:
        opcao_digitada = int(input("Selecione uma opção:\n"))
        print("\nVocê escolheu a opção:", opcao_digitada)
        match opcao_digitada:
            case 1:
                print("Você escolheu cadastrar seu restaurante.")
            case 2:
                print("Você escolheu listar seu restaurante.")
            case 3:
                print("Você escolheu ativar seu restaurante.")
            case 4:
                sair()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system("cls")
    chama_nome_app()
    exibir_opcoes()
    escolha_opcoes()


if __name__ == "__main__":
    main()
