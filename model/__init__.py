from sqlalchemy_utils import database_exists, create_database  # Funções para verificar e criar o banco de dados
from sqlalchemy.orm import sessionmaker  # Para criar sessões de interação com o banco de dados
from sqlalchemy import create_engine  # Para estabelecer a conexão com o banco de dados
import os  # Para operações com o sistema de arquivos

from model.base import Base  # Classe base para os modelos ORM
from model.historico import Historico  # Modelo que representa a tabela 'Historico'

db_path = "database/"  # Diretório onde o banco de dados será armazenado

# Cria o diretório do banco de dados se ele não existir
if not os.path.exists(db_path):
    os.makedirs(db_path)

db_url = f'sqlite:///{db_path}db.sqlite3'  # URL de conexão para o banco de dados SQLite

# Cria o engine que gerencia a conexão com o banco de dados
engine = create_engine(db_url, echo=False)

# Cria uma fábrica de sessões vinculada ao engine
Session = sessionmaker(bind=engine)

# Verifica se o banco de dados existe; se não, cria-o
if not database_exists(engine.url):
    create_database(engine.url)

# Cria todas as tabelas definidas nos modelos ORM, caso não existam
Base.metadata.create_all(engine)
