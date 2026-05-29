class Plataforma:
    def __init__(self, nome):
        self.nome = nome
        self.midias = []

    def adicionar_midia(self, midia):
        self.midias.append(midia)

    def listar_midias(self):
        print(f"\n Mídias disponíveis em '{self.nome}':")
        for midia in self.midias:
            midia.mostrar_info()

    def reproduzir_todas(self):
        print(f"\n Reproduzindo todas as mídias de '{self.nome}':")
        for midia in self.midias:
            midia.reproduzir()
