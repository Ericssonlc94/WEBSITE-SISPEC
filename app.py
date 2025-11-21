<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
=======
>>>>>>> 6c0d003d7f294dcf44c0e7fb1504440f525c684f
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
<<<<<<< HEAD
    try:
        url = "https://www8.receita.fazenda.gov.br/simplesnacional/noticias/TodasNoticias.aspx"
        base_url = "https://www8.receita.fazenda.gov.br/simplesnacional/noticias/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        
        noticias_list = []
        
        news_container = soup.find('div', id='ctl00_contentPlaceH_divNoticias')

        if not news_container:
            return jsonify([{"titulo": "Erro ao buscar notícias", "link": "#", "descricao": "Não foi possível encontrar o contêiner de notícias.", "data": ""}])

        news_rows = news_container.find_all('div', class_='row', recursive=False)

        for i in range(0, len(news_rows), 2):
            title_row = news_rows[i]
            
            if i + 1 < len(news_rows):
                content_row = news_rows[i+1]

                title_link = title_row.find('a', class_='azulClaro')
                if title_link:
                    titulo = title_link.get_text(strip=True)
                    link_relative = title_link.get('href')
                    link_absolute = base_url + link_relative if link_relative else "#"

                    spans = content_row.find_all('span')
                    if len(spans) == 2:
                        data = spans[0].get_text(strip=True)
                        descricao = spans[1].get_text(strip=True)
                    else:
                        data = ''
                        descricao = content_row.get_text(strip=True)


                    noticias_list.append({
                        "titulo": titulo,
                        "link": link_absolute,
                        "descricao": descricao,
                        "data": data
                    })

        return jsonify(noticias_list)

    except requests.exceptions.RequestException as e:
        return jsonify([{"titulo": "Erro de conexão", "link": "#", "descricao": f"Não foi possível conectar ao portal de notícias.", "data": ""}])
    except Exception as e:
        return jsonify([{"titulo": "Erro inesperado", "link": "#", "descricao": f"Ocorreu um erro ao processar as notícias: {e}", "data": ""}])

=======
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
>>>>>>> 6c0d003d7f294dcf44c0e7fb1504440f525c684f

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
