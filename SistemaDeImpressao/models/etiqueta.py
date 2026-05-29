class Etiqueta:
    def __init__(self, destinatario, endereco):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self) -> None:
        print(f" [ETIQUETA] Para: {self.destinatario} | Endereço: {self.endereco}")
