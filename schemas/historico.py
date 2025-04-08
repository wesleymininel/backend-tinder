from pydantic import BaseModel  # Base para criação e validação de dados
from datetime import date
from typing import Optional, List
from model.historico import Historico  # Importa o modelo ORM

# Schema para criação de um novo registro no histórico
class HistoricoSchema(BaseModel):
    picture: str="https://randomuser.me/api/portraits/women/11.jpg"
    firstname: str="Andressa"
    lastname: str="Barros"
    age: int=73
    gender: str="female"
    state: str="Paraná"
    like: str="Yes"

# Schema para busca de um histórico pelo primeiro nome
class HistoricoBuscaSchema(BaseModel):
    firstname: str="Andressa"

# Schema para representar uma lista de históricos
class ListagemHistoricosSchema(BaseModel):
    historicos: List[HistoricoSchema]

# Função para exibir vários históricos
def apresenta_historicos(historicos: List[Historico]):
    result = []
    for historico in historicos:
        result.append({
           "picture": historico.picture,
            "firstname": historico.firstname,
            "lastname": historico.lastname,
            "age": historico.age,
            "gender": historico.gender,
            "state": historico.state,
            "like": historico.like,
        })
    return {"historicos": result}

# Schema para visualização de um único histórico
class HistoricoViewSchema(BaseModel):
    picture: str="https://randomuser.me/api/portraits/women/11.jpg"
    firstname: str="Andressa"
    lastname: str="Barros"
    age: int=73
    gender: str="female"
    state: str="Paraná"
    like: str="Yes"

# Schema usado ao deletar um histórico
class HistoricoDelSchema(BaseModel):
    mesage: str
    firstname: str 

# Função para exibir um único histórico
def apresenta_historico(historico: Historico):
    return {
           "picture": historico.picture,
            "firstname": historico.firstname,
            "lastname": historico.lastname,
            "age": historico.age,
            "gender": historico.gender,
            "state": historico.state,
            "like": historico.like,
     }

# Schema para atualização do campo 'like'
class HistoricoUpdateLikeSchema(BaseModel):
    firstname: str
    like: str
