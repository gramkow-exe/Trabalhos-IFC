#Erro caso o usuário não tenha adicionado nada
class ZeroDados(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)