import banco
import time

class Flor:
    #Estrutura em PO das plantas 
    def __init__(self, nome_p, nome_c, valor, quantidade, caracteristica, tipo
) -> None:
        self.nome_p = nome_p
        self.nome_c = nome_c
        self.valor = valor
        self.quantidade = quantidade
        self.caracteristica = caracteristica
        self.tipo = tipo

class Tipo:
    #Estrutura em PO dos tipos de plantas 
    def __init__(self, nome, clima, local) -> None:
        self.nome = nome
        self.clima = clima
        self.local = local
    
class Floricultura:
    def __init__(self) -> None:
        self.banco = banco.Banco()

    def adicionar_flor(self):
        try:
            #Recolhe as informações para criação de um objeto flor
            nova_flor = [input("Nome popular da flor: "), input("Nome científico da flor: "), float(input("Valor da unidade: ")), int(input("Quantidade de flores: ")), input("Características ou observações: ")]
            
            #Retorna a quantidade de tipos cadastrados para não gerar erros
            qtde_tipos = self.banco.retornar_quantidade("tipos").fetchone()
            
            if qtde_tipos[0] == 0:
                print("Nenhum tipo criado!")

                print("Redirecionando à criação de tipos...")
                time.sleep(1)
                self.adicionar_tipo()
                time.sleep(0.5)

            self.banco.conectar()
            #Mostra os tipos ao usuários para melhor inserção na tabela flores
            tipos = self.banco.conexao.execute("select * from tipos")
            self.banco.desconectar()
            for i in tipos:
                print(f"{i[0]} - {i[1]}")

            #Recebe o tipo da flor e verifica sua existência
            tipo = int(input("Tipo da flor (0 para cancelar):"))
            tipo_encontrado = self.banco.verificar_exitencia("tipos", tipo , 'id').fetchone()
            if tipo_encontrado[0] > 0:  
                nova_flor.append(tipo)
                flor = Flor(nova_flor[0], nova_flor[1], nova_flor[2], nova_flor[3], nova_flor[4], nova_flor[5])
                select = self.banco.verificar_exitencia("flores", flor.nome_c, 'nome_c').fetchone()
                if select[0] > 0:
                    print("Esta flor ja existe")
                else:
                    self.banco.adicionar_flor(flor)
                    print("")
                    print("Caso não haja nenhum erro, a flor sera adcionada em breve!")
            else:
                print("Tipo da planta não encontrado!")
            

        except ValueError:
            print("Valor incorreto, recomeçando...")
            time.sleep(0.5)
            self.adicionar_flor()
       
        

    def remover_flor(self):
        #Verifica se existe alguma flor na tabela
        qtde = self.banco.retornar_quantidade("flores").fetchone()
        if qtde[0] != 0:
            self.banco.mostra_flores()
            print("")
            #Recebe o nome da flor a ser excluída
            flor = input("Nome cientifico da flor a ser excluida: ")

            #Verifica a existência no banco e a apaga
            select = self.banco.verificar_exitencia("flores", flor, "nome_c").fetchone()
            if select[0] > 0:
                self.banco.remover_flor(flor)
                print("Flor excluída")
            else:
                print("Flor não encontrada!")
        else:
            print("Nenhuma flor cadastrada!")

    def adicionar_tipo(self):
        #Recebe valores de um novo tipo
        novo_tipo = [input("Nome do tipo: "), input("Clima do tipo: "), input("Localização do tipo: ")]

        #Verifica existência no banco e a adciona
        select = self.banco.verificar_exitencia("tipos", novo_tipo[0], "nome").fetchone()
        if select[0] == 0:
            self.banco.adicionar_tipo(novo_tipo)
        else:
            print("Tipo ja existente!")

    def remover_tipo(self):
        self.banco.mostra_flores()
        print("")
        #Recebe o nome do tipo a ser excluído
        nome = input("Nome do tipo a ser excluido: ")

        #Verifica a existencia no banco e a apaga
        select = self.banco.verificar_exitencia("tipos", nome.lower() , "nome").fetchone()
        if select[0] > 0:
            self.banco.remover_tipo(nome)
            print("Tipo excluído!")
            print("As flores continuarão disponiveis!")
        else:
            print("Tipo não existente!")

    

