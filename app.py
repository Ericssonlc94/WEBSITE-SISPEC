from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/noticias')
def noticias():
    # Retorna as notícias em formato HTML (página completa)
    return render_template('index.html')

@app.route('/api/noticias')
def api_noticias():
    # Retorna as notícias em formato JSON para uso via JavaScript
    noticias = [
        {
            "titulo": "Novas regras para MEIs em 2025",
            "link": "#",
            "descricao": "Entenda como as alterações nas regras para Microempreendedores Individuais afetam sua empresa..."
        },
        {
            "titulo": "Benefícios do Simples Nacional",
            "link": "#",
            "descricao": "Veja como optar pelo regime simplificado pode reduzir sua carga tributária..."
        },
        {
            "titulo": "Declaração de Imposto de Renda",
            "link": "#",
            "descricao": "Principais cuidados ao declarar seus rendimentos e deduções este ano..."
        }
    ]
    return jsonify(noticias)

@app.route('/servicos')
def servicos():
    return render_template('index.html')

@app.route('/simuladores')
def simuladores():
    return render_template('index.html')

@app.route('/quem-somos')
def quem_somos():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
