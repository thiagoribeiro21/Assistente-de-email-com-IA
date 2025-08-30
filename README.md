<img src="static/images/e-mail%20(1).png" alt="Logo do Projeto">

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

---

## Etiquetas

[![Licença](https://img.shields.io/badge/licença-MIT-blue)](./LICENSE)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Último Commit](https://img.shields.io/github/last-commit/thiagoribeiro21/autoU)

<br>

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HuggingFace](https://img.shields.io/badge/huggingface-yellow?style=for-the-badge&logo=huggingface&logoColor=black)

---

## Funcionalidades

- 📧 **Análise de Email:** Cole o texto ou envie um arquivo para análise automática.
- 🤖 **Classificação com IA:** O sistema identifica se o email é produtivo ou improdutivo.
- ✉️ **Sugestão de Resposta:** Receba uma resposta pronta para copiar e colar.
- 📂 **Upload de Arquivos:** Suporte a `.txt` e `.pdf`.
- 💻 **Interface Responsiva:** Visual moderno e adaptável a qualquer dispositivo.

---

## Stack utilizada

**Front-end:** HTML5, CSS3, JavaScript  
**Back-end:** Python, Flask  
**IA:** Hugging Face Transformers (facebook/bart-large-mnli)  
**Outros:** PyPDF2 (leitura de PDF)

---

## Screenshots

<img src="static/images/screenshot-form.png" alt="Formulário de análise de email" width="400">
<img src="static/images/screenshot-resultado.png" alt="Resultado da análise" width="400">

---

## ⚙️ Instalação e Execução Local

Siga os passos abaixo para rodar o projeto localmente:

### 1. Clone o repositório

```bash
git clone https://github.com/thiagoribeiro21/autoU.git
```
