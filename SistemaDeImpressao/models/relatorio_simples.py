class RelatorioSimples:
    def __init__(self, titulo):
        self.titulo = titulo

    def imprimir(self) -> None:
        print(f" [RELATÓRIO] Título: {self.titulo}")
