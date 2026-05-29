from models.funcionario_assalariado import FuncionarioAssalariado
from models.funcionario_horista import FuncionarioHorista
from models.funcionario_comissionado import FuncionarioComissionado
from services.empresa import Empresa

# Criando a empresa
empresa = Empresa("TechCorp")

# Criando os funcionários
f1 = FuncionarioAssalariado("Ana", "111.111.111-11", 3000)
f2 = FuncionarioHorista("Carlos", "222.222.222-22", 40, 25)
f3 = FuncionarioComissionado("Maria", "333.333.333-33", 10000, 10)

# Adicionando à empresa
empresa.adicionar_funcionario(f1)
empresa.adicionar_funcionario(f2)
empresa.adicionar_funcionario(f3)

# Listando e exibindo folha
empresa.listar_funcionarios()
empresa.mostrar_folha_pagamento()
