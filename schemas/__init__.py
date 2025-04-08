# Importa os esquemas relacionados ao histórico do módulo 'schemas.historico'
from schemas.historico import (
    HistoricoSchema,           # Esquema para validar e serializar dados do histórico
    HistoricoBuscaSchema,      # Esquema para validar parâmetros de busca de históricos
    HistoricoViewSchema,       # Esquema para formatar a visualização de um histórico
    ListagemHistoricosSchema,  # Esquema para listar múltiplos históricos
    HistoricoDelSchema,        # Esquema para validar a deleção de um histórico
    apresenta_historicos,      # Função para apresentar uma lista de históricos
    apresenta_historico        # Função para apresentar um único histórico
)

# Importa o esquema de erro do módulo 'schemas.error'
from schemas.error import ErrorSchema  # Esquema para padronizar respostas de erro


