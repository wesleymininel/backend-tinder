from sqlalchemy import Column, String, Integer, DateTime  # Importa os tipos de coluna do SQLAlchemy
from datetime import datetime  # Importa a função para obter a data e hora atuais
from typing import Union  # Importa Union para anotações de tipo opcionais

from model import Base  # Importa a classe base declarativa para os modelos ORM

class Historico(Base):
    __tablename__ = 'historico'  # Define o nome da tabela no banco de dados

    id = Column("pk_historico", Integer, primary_key=True)  # Coluna de chave primária
    picture = Column(String(140))  # URL ou caminho para a imagem do perfil
    firstname = Column(String(50))  # Primeiro nome do usuário
    lastname = Column(String(50))  # Sobrenome do usuário
    age = Column(Integer)  # Idade do usuário
    gender = Column(String(50))  # Gênero do usuário
    state = Column(String(50))  # Estado de residência do usuário
    like = Column(String(10))  # Indica se foi dado 'like' ou 'dislike'
    date_insert = Column(DateTime, default=datetime.now)  # Data e hora da inserção

    def __init__(self, picture: str, firstname: str, lastname: str, age: int, gender: str, state: str, like: str,
                 date_insert: Union[DateTime, None] = None):
        """
        Inicializa uma instância da classe Historico.

        :param picture: URL ou caminho para a imagem do perfil.
        :param firstname: Primeiro nome do usuário.
        :param lastname: Sobrenome do usuário.
        :param age: Idade do usuário.
        :param gender: Gênero do usuário.
        :param state: Estado de residência do usuário.
        :param like: Indica se foi dado 'like' ou 'dislike'.
        :param date_insert: Data e hora da inserção (opcional).
        """
        self.picture = picture
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.state = state
        self.like = like
        self.date_insert = date_insert if date_insert else datetime.now()
