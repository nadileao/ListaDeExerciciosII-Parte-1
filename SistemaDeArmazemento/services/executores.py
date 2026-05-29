from models.armazenador import Armazenador
from models.salvavel import Salvavel

def executar_salvamento_formal(armazenador: Armazenador, dado) -> None:
    print(" [FORMAL - ABC]")
    armazenador.salvar(dado)

def executar_salvamento_flexivel(objeto: Salvavel, dado) -> None:
    print(" [FLEXÍVEL - Protocol]")
    objeto.salvar(dado)
