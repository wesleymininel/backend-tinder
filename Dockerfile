# Usa a imagem oficial do Python 3.9 como base
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner como '/app'
WORKDIR /app

# Copia o arquivo 'requirements.txt' para o diretório de trabalho
COPY requirements.txt ./

# Instala as dependências listadas em 'requirements.txt' sem armazenar cache
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Comando para iniciar a aplicação Flask, configurando-a para ouvir em todas as interfaces de rede
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]