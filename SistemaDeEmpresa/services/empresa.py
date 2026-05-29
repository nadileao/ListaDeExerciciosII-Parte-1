class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\n Funcionários de '{self.nome}':")
        for funcionario in self.funcionarios:
            funcionario.mostrar_dados()

    def mostrar_folha_pagamento(self):
        print(f"\n Folha de Pagamento de '{self.nome}':")
        total = 0
        for funcionario in self.funcionarios:
            pagamento = funcionario.calcular_pagamento()
            total += pagamento
            print(f"  {funcionario.nome} → R$ {pagamento:.2f}")
        print(f"\n  Total a pagar: R$ {total:.2f}")
