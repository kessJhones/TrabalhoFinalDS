from flask import Flask, redirect, url_for, escape, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        player = request.form.get('players')
        nome_personagem = request.form['nome']
        return redirect(url_for('dados', nome = nome_personagem, X = player))

    return render_template('index.html',
        title='Página Inicial',
    )

@app.route('/Dados/<nome><X>', methods = ['POST', 'GET'])
def dados(nome, X):
    return render_template('dados.html',
        title='Ficha',
        nome = nome,
        X = X,
    )

if __name__ == '__main__':
    app.run(debug=True)
