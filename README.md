<img src="static/images/e-mail%20(2).png" alt="Logo do Projeto">

# Assistente de Email com IA

Um sistema web inteligente para análise e sugestão de respostas automáticas para emails, utilizando Python, Flask e modelos de IA da Hugging Face.

---

## Sobre o Projeto

O **Assistente de Email com IA** é uma aplicação web que permite ao usuário colar o texto de um email ou enviar um arquivo `.txt` ou `.pdf`. O sistema utiliza inteligência artificial para classificar o email como **Produtivo** ou **Improdutivo** e sugere uma resposta automática personalizada.

Principais características:

- **Classificação Inteligente:** Utiliza o modelo zero-shot da Hugging Face para identificar a categoria do email.
- **Sugestão de Resposta:** Gera automaticamente uma resposta adequada conforme a categoria.
- **Upload de Arquivos:** Aceita arquivos `.txt` e `.pdf` para análise.
- **Interface Responsiva:** Desenvolvida com HTML5, CSS3 e JavaScript.
- **Backend em Python:** Utiliza Flask para servir a aplicação e processar as requisições.
- **Deploy com Docker e Gunicorn:** Pronto para rodar em containers e ambientes de produção.
- **Deploy público:** Disponível em [https://thiago-ribeiro-21-assistente-email-com-ia.hf.space/](https://thiago-ribeiro-21-assistente-email-com-ia.hf.space/)

---

## Etiquetas

[![Licença](https://img.shields.io/badge/licença-MIT-blue)](./LICENSE)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Último Commit](https://img.shields.io/github/last-commit/thiagoribeiro21/Assistente-de-email-com-IA)

<br>

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![HuggingFace Spaces](https://img.shields.io/badge/HuggingFace%20Spaces-yellow?style=for-the-badge&logo=huggingface&logoColor=black)

---

## ✨ Deploy Online

Acesse a versão pública do projeto:  
🔗 [https://thiago-ribeiro-21-assistente-email-com-ia.hf.space/](https://thiago-ribeiro-21-assistente-email-com-ia.hf.space/)

---

## Funcionalidades

- 📧 **Análise de Email:** Cole o texto ou envie um arquivo para análise automática.
- 🤖 **Classificação com IA:** O sistema identifica se o email é produtivo ou improdutivo.
- ✉️ **Sugestão de Resposta:** Receba uma resposta pronta para copiar e colar.
- 📂 **Upload de Arquivos:** Suporte a `.txt` e `.pdf`.
- 💻 **Interface Responsiva:** Visual moderno e adaptável a qualquer dispositivo.
- 🐳 **Deploy com Docker:** Pronto para rodar em containers.

---

## Stack utilizada

**Front-end:** HTML5, CSS3, JavaScript  
**Back-end:** Python, Flask  
**IA:** Hugging Face Transformers (facebook/bart-large-mnli)  
**Outros:** PyPDF2, Docker, Gunicorn

---

## Screenshots

<img src="static/images/screenshot-home.png" alt="Formulário de análise de email" width="400">
<img src="static/images/screenshot-response.png" alt="Resultado da análise" width="400">

---

## ⚙️ Instalação e Execução Local

### 1. Clone o repositório

```bash
git clone https://github.com/thiagoribeiro21/Assistente-de-email-com-IA.git
```

### 2. Instale as dependências

Recomenda-se o uso de um ambiente virtual:

```bash
cd Assistente-de-email-com-IA
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Execute o servidor Flask

```bash
python app.py
```

Acesse em [http://localhost:5000](http://localhost:5000) ou [http://localhost:5001](http://localhost:5001) dependendo da porta configurada.

---

## 🐳 Rodando com Docker

Você pode rodar o projeto em um container Docker facilmente:

```bash
docker build -t assistente-email-ia .
docker run -p 7860:7860 assistente-email-ia
```

Depois, acesse [http://localhost:7860](http://localhost:7860)

---

## Aprendizados

Esse projeto marcou minha transição para o desenvolvimento full-stack. Nele, criei uma aplicação web completa do zero: construí um backend em Python com Flask e integrei um modelo de Processamento de Linguagem Natural (PNL) da Hugging Face para classificar textos de diferentes fontes, como entradas diretas, arquivos .txt e .pdf. Além da parte de programação, cuidei de todo o ciclo de vida da aplicação, desde a conteinerização com Docker até o deploy em nuvem. Foi uma experiência prática que consolidou minha capacidade de levar uma solução de IA do papel para a produção.

---

## 👨‍💻 Autor

Feito por **Thiago Ribeiro**

- **LinkedIn:** https://www.linkedin.com/in/thiagorib21
- **Email:** thiago.ribeiro2003@hotmail.com
- **GitHub:** https://github.com/thiagoribeiro21

---

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
