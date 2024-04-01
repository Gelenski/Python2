print("Programa Expresso")
print("1 - Cadastrar restaurante")
print("2 - Listar restaurante")
print("3 - Ativar restaurante")
print("4 - Sair")
opcao_digitada = int(input("Selecione uma opção:\n"))
print("Você escolheu a opção:", opcao_digitada)
match opcao_digitada:
    case 1:
        print("Você escolheu cadastrar seu restaurante.")
    case 2:
        print("Você escolheu listar seu restaurante.")
    case 3:
        print("Você escolheu ativar seu restaurante.")
    case 4:
        print("Você escolheu sair.")
