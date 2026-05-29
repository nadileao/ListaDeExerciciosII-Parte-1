from models.armazenador import Armazenador

class ArmazenadorBanco(Armazenador):

    def salvar(self, dado) -> None:
        print(f"  [BANCO] Salvando dado: '{dado}'")
