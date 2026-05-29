from models.armazenador_arquivo import ArmazenadorArquivo
from models.armazenador_banco import ArmazenadorBanco
from models.armazenador_nuvem import ArmazenadorNuvem
from services.executores import executar_salvamento_formal
from services.executores import executar_salvamento_flexivel

# Criando os objetos
arquivo = ArmazenadorArquivo()
banco   = ArmazenadorBanco()
nuvem   = ArmazenadorNuvem()

dado = "Relatório de Vendas 2025"

# Parte A — ABC (apenas quem herda de Armazenador)
print("\n Testando com ABC:\n")
executar_salvamento_formal(arquivo, dado)
executar_salvamento_formal(banco, dado)

# Parte B — Protocol (qualquer objeto com salvar())
print("\n Testando com Protocol:\n")
executar_salvamento_flexivel(arquivo, dado)
executar_salvamento_flexivel(banco, dado)
executar_salvamento_flexivel(nuvem, dado)   
