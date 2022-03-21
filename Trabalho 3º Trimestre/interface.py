import main

while True:
    if __name__ == "__main__":
        floricultura = main.Floricultura()
        print('')
        print(" - - Igor's Flowers - - ")
        print("------------------------")
        print("1 - Adicionar Flor------")
        print("2 - Remover Flor--------")
        print("3 - Adicionar Tipo------")
        print("4 - Remover Tipo--------")
        print("5 - Mostra Flores/Tipos-")
        print("------------------------")
        escolha = input("Digite: ")
        print('')
        if escolha == "1":
            floricultura.adicionar_flor()
        elif escolha == "2":
            floricultura.remover_flor()
        elif escolha == "3":
            floricultura.adicionar_tipo()
        elif escolha == "4":
            floricultura.remover_tipo()
        elif escolha == "5":
            floricultura.banco.mostra_flores()
        else:
            print("Função não encontrada!")
