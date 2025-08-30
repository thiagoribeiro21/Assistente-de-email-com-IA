# Define a imagem base do Python que vamos usar
FROM python:3.9-slim

# Cria e define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para dentro do container
COPY requirements.txt .

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o resto do seu código (app.py, templates/, etc.) para o container
COPY . .

# Expõe a porta que a aplicação vai usar. O Hugging Face usa a 7860 por padrão.
EXPOSE 7860

# O comando que será executado quando o container iniciar.
# Usamos o Gunicorn para rodar nosso app Flask.
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]