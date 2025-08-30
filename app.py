# app.py
import os
from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import PyPDF2
from io import BytesIO

# Inicializa o Flask
app = Flask(__name__)

# Carrega os modelos de IA da Hugging Face
# Usamos um modelo de "zero-shot-classification" que é flexível para classificar com base em rótulos que definimos na hora.
# Isso evita a necessidade de treinar um modelo específico.
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Rótulos para classificação
CATEGORIES = ["Produtivo", "Improdutivo"]

# Rota principal que renderiza a interface web
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o email
@app.route('/processar', methods=['POST'])
def processar_email():
    email_text = ""
    
    # Verifica se foi enviado um arquivo
    if 'email_file' in request.files and request.files['email_file'].filename != '':
        file = request.files['email_file']
        filename = file.filename.lower()
        
        try:
            if filename.endswith('.txt'):
                email_text = file.read().decode('utf-8')
            elif filename.endswith('.pdf'):
                # Lê o conteúdo do PDF
                pdf_reader = PyPDF2.PdfReader(BytesIO(file.read()))
                for page in pdf_reader.pages:
                    email_text += page.extract_text()
            else:
                return jsonify({'error': 'Formato de arquivo não suportado. Use .txt ou .pdf.'}), 400
        except Exception as e:
            return jsonify({'error': f'Erro ao ler o arquivo: {str(e)}'}), 500

    # Verifica se foi enviado texto diretamente
    elif 'email_text' in request.form:
        email_text = request.form['email_text']
        
    if not email_text:
        return jsonify({'error': 'Nenhum texto ou arquivo foi fornecido.'}), 400

    # --- Etapa de Classificação com IA ---
    try:
        classification_result = classifier(email_text, candidate_labels=CATEGORIES)
        
        # O resultado vem ordenado por score, então o primeiro item é a categoria mais provável
        top_category = classification_result['labels'][0]
        confidence_score = classification_result['scores'][0]

    except Exception as e:
        return jsonify({'error': f'Erro durante a classificação: {str(e)}'}), 500

    # --- Etapa de Geração de Resposta ---
    suggested_reply = ""
    if top_category == "Produtivo":
        suggested_reply = (
            "Prezado cliente,\n\n"
            "Agradecemos pelo seu contato. Recebemos sua solicitação e já estamos analisando.\n"
            "Em breve, um de nossos especialistas retornará com mais informações.\n\n"
            "Atenciosamente, AutoU"
        )
    elif top_category == "Improdutivo":
        suggested_reply = (
            "Olá!\n\n"
            "Obrigado pela sua mensagem!\n\n"
            "Abraços, AutoU."
        )

    # Retorna o resultado em formato JSON
    return jsonify({
        'categoria': top_category,
        'confianca': f"{confidence_score:.2%}",
        'sugestao_resposta': suggested_reply
    })

if __name__ == '__main__':
    # A porta é lida da variável de ambiente PORT, útil para o deploy
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port, debug=True)