from gerenciador import Loja

loja = Loja()
saida = False

while not saida:
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Mostrar produtos")
    print("4 - Passar dia")
    print("5 - Gravar Produtos")
    print("6 - Recuperar Produtos")
    print("7 - Sair")

    escolha = int(input("Digite a escolha: "))
    if escolha == 1:
        loja.adicionar_produto()
    elif escolha == 2:
        loja.excluir_produto()
    elif escolha == 3:
        loja.mostrar_produtos()
    elif escolha == 4:
        loja.passar_dia()
    elif escolha == 5:
        loja.gravar()
    elif escolha == 6:
        loja.recuperar()
    elif escolha == 7:
        saida = True

    

