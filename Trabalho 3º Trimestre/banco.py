import sqlite3
import time
import erros
from sqlite3.dbapi2 import Cursor
class Banco:
    def __init__(self) -> None:
        self.conexao = None
     
    def conectar(self):
        #Conexão com o banco de dados para evitar tráfego mútuo
        if self.conexao == None:
            self.conexao = sqlite3.connect("Igor_Flores.db")
        else:
            print("Ja está conectado!")

    def desconectar(self):
        #Desconexão com o banco de dados para evitar tráfego mútuo
        if self.conexao == None:
            print("Ja está desconectado!")
        else:
            self.conexao = None

    def adicionar_flor(self, flor):
        #Adciona uma flor com os valores entregues pelo usuário na função 'adcionnar_flor' do arquivo main
        self.conectar()
        values = [flor.nome_p, flor.nome_c, flor.valor, flor.quantidade, flor.caracteristica, flor.tipo]
        tipos = self.conexao.execute(f"select count(*) from tipos where id = ?", [flor.tipo]).fetchone()
        if tipos[0] > 0:
            self.conexao.execute(f"Insert into Flores (nome_p, nome_c, valor, quantidade, caracteristica, tipo_id) values(?,?,?,?,?,?)",values)
        else:
            print("Tipo não encontrado!")
        self.conexao.commit()
        self.desconectar()

    def remover_flor(self, flor):
        #Remove uma flor no banco com o nome passado a função
        self.conectar()
        self.conexao.execute("delete from flores where nome_c = ?", [flor])
        self.conexao.commit()
        self.desconectar()

    def adicionar_tipo(self, values):
        #Inseri um novo tipo no banco com os valores passados a função
        self.conectar()
        self.conexao.execute(f"insert into Tipos (nome, clima, local) values(?, ?, ?)", values)
        self.conexao.commit()
        self.desconectar()

    def remover_tipo(self, nome):
        #Remove um tipo no banco com o nome passado a função
        self.conectar()
        self.conexao.execute(f"delete from tipos where nome = ? ", [nome])
        self.conexao.commit()
        self.desconectar()

    def verificar_exitencia(self, tabela, nome, parametro) -> sqlite3.Cursor:
        #A variável tabela e parâmetro não precisam ser colocadas na string com o ? pois não são escritas pelo usuário
        self.conectar()
        retorno = self.conexao.execute(f"select count(*) from {tabela} where {parametro} = ? ", [nome])
        self.desconectar()
        return retorno

    

    def mostra_flores(self):
        dados = self.retornar_quantidade("flores").fetchone()
        self.conectar()
        try:
            if dados[0] != 0:
                tipos = self.conexao.execute("Select * from tipos")
                flores = self.conexao.execute("Select * from flores")

                print("Tipos:")
                for i in tipos:
                    time.sleep(0.3)
                    print(f"{i[0]} - {i[1]}")

                print('')

                time.sleep(0.5)
                print("Flores:")
                for i in flores:
                    time.sleep(0.3)
                    print(f"{i[0]} - {i[2]}")
                
                print('')
                self.desconectar()
                resposta = input("Clique enter para retornar! Ou digite o nome cientifico de uma flor ou tipo: ")


                if resposta != "":
                    select = self.verificar_exitencia("flores", resposta, "nome_c").fetchone()
                    self.conectar()
                    if select[0] > 0:
                        infos = self.conexao.execute("select * from flores where nome_c = ?", [resposta]).fetchone()
                        #Verifica se o tipo foi excluido
                        tipo_existe = self.conexao.execute("select count(*) from tipos where id = ?", [infos[6]]).fetchone()
                        print('')
                        #Mostra as infos da flor
                        if tipo_existe[0] != 0:
                            tipo = self.conexao.execute("select nome from tipos where id = ?", [infos[6]]).fetchone()
                            print(f''' Nome popular: {infos[1]}\n Nome científico: {infos[2]}\n Valor: {infos[3]}\n Quantidade: {infos[4]}\n Características: {infos[5]}\n Tipo: {tipo[0]}
                        ''')
                        else:
                            print(f''' Nome popular: {infos[1]}\n Nome científico: {infos[2]}\n Valor: {infos[3]}\n Quantidade: {infos[4]}\n Características: {infos[5]}''')
                        time.sleep(0.5)
                        self.desconectar()
                    else:
                        select = self.verificar_exitencia("tipos", resposta, "nome").fetchone()
                        self.conectar()
                        #Mostra as infos do tipo
                        infos = self.conexao.execute("select * from tipos where nome = ?", [resposta]).fetchone()
                        print("")
                        print(f'''Nome do tipo: {infos[1]}\nClima do tipo: {infos[2]}\nLocalização: {infos[3]} ''')
                        time.sleep(0.5)
                        self.desconectar()
                
            else:
                raise erros.ZeroDados()
        except erros.ZeroDados:
            print("Nenhum dado cadastrado!")



    def retornar_quantidade(self, tabela):
        #Funçao que retorna a quantidade de inserções em uma tabela
        #Tira a possibilidade de erros com zero dados
        self.conectar()
        retorno = self.conexao.execute(f"select count(*) from {tabela}")
        self.desconectar()
        return retorno


#Criação do banco de dados

#a = Banco()
#a.conectar()
#sql = open("tabelas.sql", "r").read().split(';')
#for comando in sql:
#    a.conexao.execute(comando)
#a.desconectar()


