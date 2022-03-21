from data import Data, Calendario
import produto
import time

class Loja():
    def __init__(self) -> None:
        self.produtos = []
        self.produtos_vencidos = []

        print("")
        print("Bem vindo!")

        dia_atual = input("Digite a data atual: ")
        while len(dia_atual) != 10 or not(dia_atual[2] == "/" and dia_atual[5] == "/"):
            print("Data curta ou inválida!")
            dia_atual = input("Digite novamente: ")
        
        data = Data(dia_atual)
            
        while not Calendario.verificar_data(data):
            print("Data Inválida!")
            dia_atual = input("Digite a data atual: ")
            if len(dia_atual) == 10:
                if dia_atual[2] == "/" and dia_atual[5] == "/":
                    data = dia_atual
                    data = Data(dia_atual)
            
        self.dia = Calendario.retornar_data(data)

    def adicionar_produto(self):
        print("Vamos começar!")

        time.sleep(0.5)

        print("")
        nome = input("Digite o nome do novo produto: ")

        preco = float(input("Preço sugerido: "))

        quantidade = input("Digite a quantidade (**kg ou **un): ")

        validade = input("Digite a validade (dd/mm/aaaa): ")

        tipo = input("O produto é uma verdura ou fruta? ")
        while not (tipo ==  "verdura" or tipo == "fruta"):
            tipo = input("Valor invalido (verdura ou fruta): ")

        refrigerado = input("O produto é refrigerado? (sim ou não) ")
        while not (refrigerado == "sim" or refrigerado == "não"):
            refrigerado = input("Valor invalido (sim ou não): ")

        if tipo == "verdura":
            if refrigerado == "sim":
                temperatura = input("Digite a temperatura sugerida: ")
                self.produtos.append(produto.Verdura_Refrigerada(nome, preco, quantidade, validade, temperatura))
            else:
                self.produtos.append(produto.Verdura(nome, preco, quantidade, validade))
        else:
            if refrigerado == "sim":
                temperatura = input("Digite a temperatura sugerida: ")
                self.produtos.append(produto.Fruta_Refrigerada(nome, preco, quantidade, validade, temperatura))
            else:
                self.produtos.append(produto.Fruta(nome, preco, quantidade, validade))


    def procurar_produto(self, nome):
        conclusao = False
        for i in self.produtos:
            if nome == i.nome:
                return i
                conclusao = True
        
        if conclusao == False:
            return False
        
        
    def excluir_produto(self):
        print("Produtos:")
        for i in self.produtos:
            print(f"- {i.nome}")
        excluir = input("Qual o produto a ser excluido:")
        produto = self.procurar_produto(excluir)

        if produto != False:
            self.produtos.remove(produto)
        else:
            print("Produto não encontrado!")

    def mostrar_produtos(self):
        if len(self.produtos) == 0:
            print("Sem produtos cadastrados!")
        else:
            for i in self.produtos:
                print(f"- {i.nome} / R${i.preco} / validade: {i.validade}")

    def passar_dia(self):
        atual = Data(self.dia)
        Calendario.passar_dia(atual)
        self.dia = Calendario.retornar_data(atual)
        print(self.dia)

        lista_removidos = []

        for i in self.produtos:
            if i.validade == self.dia:
                lista_removidos.append(i.nome)
                self.produtos_vencidos.append(i)
                self.produtos.remove(i)
        
        if len(lista_removidos) > 0:
            print("Produto/s removidos por validade:")
            for i in lista_removidos:
                print(f"- {i}")
        else:
            print("Nenhum produto removido!")

    def gravar(self):
        arquivo = open(input("Digite o nome do arquivo: "), "w")
        for i in self.produtos:
            if "Refrigerada" in i.tipo:
                arquivo.write(i.nome + "#" + str(i.preco) + "#" + i.quantidade + "#" + i.validade + "#" + i.temperatura + "#" + i.tipo + "\n")
            else:
                arquivo.write(i.nome + "#" + str(i.preco) + "#" + i.quantidade + "#" + i.validade + "#" + "#" + i.tipo + "\n")
        print("Produtos gravados!")

    def recuperar(self):
        arquivo = open(input("Digite o nome do arquivo: "), "r")

        for i in arquivo.readlines():
            linha = i[:-1].split("#")

            if linha[-1] == "Fruta":
                self.produtos.append(produto.Fruta(linha[0], linha[1], linha[2], linha[3]))
            elif linha[-1] == "Fruta-Refrigerada":
                self.produtos.append(produto.Fruta_Refrigerada(linha[0], linha[1], linha[2], linha[3], linha[4]))
            elif linha[-1] == "Verdura":
                self.produtos.append(produto.Verdura(linha[0], linha[1], linha[2], linha[3]))
            elif linha[-1] == "Verdura-Refrigerada":
                self.produtos.append(produto.Verdura_Refrigerada(linha[0], linha[1], linha[2], linha[3], linha[4]))
                
            
    



