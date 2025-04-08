from flask_openapi3 import OpenAPI, Info, Tag  # Importa classes para documentação OpenAPI
from flask import redirect, Flask, request, jsonify  # Importa funções essenciais do Flask
from flask_cors import CORS  # Importa extensão para habilitar CORS
from urllib.parse import unquote  # Importa função para decodificar URLs
from sqlalchemy.exc import IntegrityError  # Importa exceção para erros de integridade do banco de dados
from model import Session, Historico  # Importa a sessão do banco de dados e o modelo Historico
from logger import logger  # Importa o logger para registro de eventos
from schemas.error import ErrorSchema  # Importa esquema para respostas de erro
from schemas.historico import (
    HistoricoBuscaSchema, HistoricoDelSchema, HistoricoSchema, 
    HistoricoViewSchema, ListagemHistoricosSchema, HistoricoUpdateLikeSchema, 
    apresenta_historico, apresenta_historicos
)  # Importa esquemas e funções relacionados ao modelo Historico

# Configurações básicas da aplicação e documentação
info = Info(title="Tinder Style", version="1.0.0")  # Define informações da API para documentação
app = OpenAPI(__name__, info=info)  # Inicializa a aplicação Flask com suporte a OpenAPI
CORS(app)  # Habilita CORS para permitir requisições de diferentes origens

# Definição de tags para organização da documentação
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
historico_tag = Tag(name="Historico", description="Adição, visualização e remoção de Historicos na base")

# Tratamento de erro para requisições malformadas
@app.errorhandler(422)
def handle_unprocessable_entity(err):
    exc = getattr(err, 'exc')
    if exc:
        messages = exc.messages
    else:
        messages = ['Invalid request']
    app.logger.error(f"Erro de validação: {messages}")
    return jsonify({'errors': messages}), 422

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota para adicionar um novo histórico
@app.post('/addhistorico', tags=[historico_tag],
          responses={"200": HistoricoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_historico(form: HistoricoSchema):
    """Adiciona um Perfil visitado no Historico da base de dados.

    """
    historico = Historico(
        picture=form.picture,
        firstname=form.firstname,
        lastname=form.lastname,
        age=form.age,
        gender=form.gender,
        state=form.state,
        like=form.like)
    logger.debug(f"Adicionando historico de usuario: '{historico.firstname}'")
    try:
        session = Session()
        session.add(historico)
        session.commit()
        logger.debug(f"Adicionado historico de usuario: '{historico.firstname}'")
        return apresenta_historico(historico), 200

    except IntegrityError as e:
        error_msg = "Historico de mesmo usuario já salvo na base"
        logger.warning(f"Erro ao adicionar historico '{historico.firstname}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível salvar novo item"
        logger.warning(f"Erro ao adicionar historico '{historico.firstname}', {error_msg}")
        return {"message": error_msg}, 400

# Rota para listar todos os históricos
@app.get('/listhistoricos', tags=[historico_tag],
         responses={"200": ListagemHistoricosSchema, "404": ErrorSchema})
def get_historicos():
    """Faz a busca por todos os Historicos de Perfis Visitados/Salvos

    Retorna uma representação em forma de listagem .
    """
    logger.debug(f"Coletando historicos")
    session = Session()
    historicos = session.query(Historico).all()

    if not historicos:
        return {"historicos": []}, 200
    else:
        logger.debug(f"%d historicos encontrados" % len(historicos))
        print(historicos)
        return apresenta_historicos(historicos), 200

# Rota para deletar um histórico pelo primeiro nome
@app.delete('/delhistorico', tags=[historico_tag],
            responses={"200": HistoricoDelSchema, "404": ErrorSchema})
def del_historico(query: HistoricoBuscaSchema):
    """Deleta um Perfil visitado do Historico cadastrado.
    
    """
    historico_firstname = unquote(unquote(query.firstname))
    print(historico_firstname)
    logger.debug(f"Deletando dados sobre historico #{historico_firstname}")
    session = Session()
    count = session.query(Historico).filter(Historico.firstname == historico_firstname).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado historico #{historico_firstname}")
        return {"message": "Historico removido", "name": historico_firstname}
    else:
        error_msg = "Historico não encontrado na base"
        logger.warning(f"Erro ao deletar historico #'{historico_firstname}', {error_msg}")
        return {"message": error_msg}, 404

# Rota para buscar um histórico pelo primeiro nome
@app.get('/findhistorico', tags=[historico_tag],
         responses={"200": HistoricoViewSchema, "404": ErrorSchema})
def get_historico(query: HistoricoBuscaSchema):
    """Faz a busca por um Perfil salvo no Historico visitado.

    """
    historico_firstname = query.firstname
    logger.debug(f"Coletando dados sobre historico #{historico_firstname}")
    session = Session()
    historico = session.query(Historico).filter(Historico.firstname == historico_firstname).first()

    if not historico:
        error_msg = "Historico não encontrado"
        logger.warning(f"Erro ao buscar historico '{historico_firstname}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Historico encontrado: '{historico.firstname}'")
        return apresenta_historico(historico), 200

# Rota para atualizar o campo 'like' de um histórico
@app.put('/edithistorico', tags=[historico_tag],
         responses={"200": HistoricoViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def edit_historico_like(body: HistoricoUpdateLikeSchema):
    """Atualiza o Like de um Perfil salvo no Historico

    """
    historico_firstname = body.firstname
    novo_like = body.like
    logger.debug(f"Atualizando like do historico #{historico_firstname} para '{novo_like}'")
    session = Session()
    historico = session.query(Historico).filter(Historico.firstname == historico_firstname).first()

    if not historico:
        error_msg = "Historico não encontrado para atualização"
        logger.warning(f"{error_msg}: {historico_firstname}")
        return {"message": error_msg}, 404

    historico.like = novo_like
    session.commit()

    logger.debug(f"Historico atualizado: {historico.firstname} -> like: {historico.like}")
    return apresenta_historico(historico), 200



