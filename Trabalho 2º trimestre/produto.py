class Verdura():
    def __init__(self, nome, preco, quantidade, validade) -> None:
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.validade = validade
        self.tipo = "Verdura"

class Verdura_Refrigerada(Verdura):
    def __init__(self, nome, preco, quantidade, validade, temperatura) -> None:
        super().__init__(nome, preco, quantidade, validade)
        self.temperatura = temperatura
        self.tipo = "Verdura-Refrigerada"

class Fruta():
    def __init__(self, nome, preco, quantidade, validade) -> None:
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.validade = validade
        self.tipo = "Fruta"
    
class Fruta_Refrigerada(Fruta):
    def __init__(self, nome, preco, quantidade, validade, temperatura) -> None:
        super().__init__(nome, preco, quantidade, validade)
        self.temperatura = temperatura
        self.tipo = "Fruta-refrigerada"