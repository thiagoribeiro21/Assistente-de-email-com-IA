# Usa uma imagem base minimalista do Python 3.9
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container como /app
WORKDIR /app

# Copia o arquivo de dependências para o container
COPY requirements.txt .

# Instala as dependências do projeto sem usar o cache do pip
RUN pip install --no-cache-dir -r requirements.txt

# Define uma variável de ambiente para o cache do Hugging Face em um diretório gravável
ENV HF_HOME=/tmp/hf_cache

# Copia todos os arquivos do projeto para o diretório de trabalho no container
COPY . .

# Expõe a porta 7860 (usada por Gradio, Streamlit ou apps web)
EXPOSE 7860

# Comando para iniciar o servidor Gunicorn, ouvindo na porta 7860, usando o objeto 'app' do arquivo app.py
CMD ["gunicorn", "--bind", "0.0.0.0:7860", "app:app"]