from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/noticias')
def noticias():
    return render_template('index.html')

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