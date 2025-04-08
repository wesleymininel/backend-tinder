from pydantic import BaseModel  # Importa a classe base para a criação de modelos de dados com validação

class ErrorSchema(BaseModel):
    message: str  # Campo que armazena a mensagem de erro
