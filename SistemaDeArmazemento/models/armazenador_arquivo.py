from models.armazenador import Armazenador

class ArmazenadorArquivo(Armazenador):

    def salvar(self, dado) -> None:
        print(f" [ARQUIVO] Salvando dado: '{dado}'")
