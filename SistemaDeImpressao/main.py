from models.boleto import Boleto
from models.etiqueta import Etiqueta
from models.relatorio_simples import RelatorioSimples
from services.processador import processar_impressao

# Criando os objetos
boleto = Boleto("123456789", 250.00)
etiqueta = Etiqueta("João Silva", "Rua das Flores, 100")
relatorio = RelatorioSimples("Relatório Mensal de Vendas")

# Processando impressão de cada um
print("\nIniciando impressão:\n")
processar_impressao(boleto)
processar_impressao(etiqueta)
processar_impressao(relatorio)
