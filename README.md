# Projeto: # Projeto: MVP Backend - Arquitetura de Software - Pós-Graduação em Engenharia de Software - PUC-RIO.

Este projeto consiste em uma aplicação backend desenvolvida em Python com o framework Flask, responsável por gerenciar as interações provenientes do frontend (https://github.com/wesleymininel/frontend-tinder/) de um sistema de matching inspirado no Tinder.

Trata-se de um MVP construído como parte das atividades da disciplina de Arquitetura de Software, no curso de Pós-Graduação em Engenharia de Software da PUC-RIO.

A API expõe endpoints RESTful que permitem:

- ✅ Adicionar perfis com informações como nome, idade, gênero, estado, foto e a decisão de "like"
- 🔍 Listar todos os perfis já registrados
- 🧾 Buscar perfis por nome
- ♻️ Editar a escolha de curtir ou não (like)
- ❌ Remover perfis do histórico

Todos os dados são armazenados em um banco de dados SQLite, garantindo persistência local de forma leve e eficiente.

Essa API funciona como ponte entre o frontend que consome a API pública RandomUser.me (https://randomuser.me) e o banco de dados, registrando as decisões dos usuários e mantendo um histórico completo das interações.

---

## 👩‍💻 Como executar Localmente

Para configurar e executar a aplicação localmente, siga os passos abaixo:

1. **Clone o repositório**:
   ```sh
   git clone https://github.com/wesleymininel/backend-tinder.git
   ```

2. **Navegue até o diretório do backend**:
   ```sh
   cd backend-tinder
   ```

3. **Criando o Ambiente ENV via Terminal Linux**:
   ```sh
   python3 -m venv env
   ```

4. **Ative o ambiente virtual**:
   ```sh
   source env/bin/activate
   ```

5. **Instale as dependências necessárias**:
   ```sh
   pip install -r requirements.txt
   ```

6. **Inicie o servidor Flask**:
   ```sh
   flask run --host 0.0.0.0 --port 5000
   ```

A aplicação estará disponível em http://localhost:5000.

---

## 👩‍💻 Como executar com Docker

Alternativamente, você pode executar a aplicação utilizando Docker. Certifique-se de que o Docker está instalado em seu sistema.

1. **Clone o repositório**:
   ```sh
   git clone https://github.com/wesleymininel/backend-tinder.git
   ```
   
2. **Navegue até o diretório do backend**:
   ```sh
   cd backend-tinder
   ```

3. **Construa a imagem Docker**:
   ```sh
   sudo docker build -t backend-tinder .
   ```

4. **Execute o contêiner**:
   ```sh
   sudo docker run -p 5000:5000 backend-tinder
   ```
A aplicação estará disponível em http://localhost:5000.

---

## 🚀 Funcionalidades

Após iniciar a aplicação, você pode interagir com as seguintes rotas:​

- POST /addhistorico: Adiciona um novo histórico de usuário.​
- GET /listhistoricos: Lista todos os históricos de usuários.​
- GET /findhistorico: Busca um histórico de usuário pelo primeiro nome.​
- PUT /edithistorico: Atualiza o campo "like" de um histórico de usuário.​
- DELETE /delhistorico: Remove um histórico de usuário pelo primeiro nome.​

Utilize ferramentas como Postman ou cURL para interagir com essas rotas.​

---

## 🔍 Tecnologias Utilizadas

- **Python​**
- **Flask​**
- **SQLAlchemy​**
- **SQLite​**
- **Docker​**

---

## 📱 Estrutura de Pastas

```
backend-tinder/
├── model/
│   └── __init__.py
│   └── base.py
│   └── historico.py
├── schemas/
│   └── __init__.py
│   └── error.py
│   └── historico.jpg
├── app.py
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir, siga os passos abaixo:​

 - Faça um fork do projeto.​
 - Crie uma branch para sua feature (git checkout -b feature/nova-feature).​
 - Commit suas alterações (git commit -m 'Adiciona nova feature').​
 - Faça o push para a branch (git push origin feature/nova-feature).​
 - Abra um Pull Request.​

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.​

---

## 📫 Contato

Para mais informações, entre em contato:

 - Email: wesley.mininel@gmail.com
 - GitHub: wesleymininel





