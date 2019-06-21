from flask import Flask, redirect, url_for, escape, request, render_template, flash
import dados as dd

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        player = request.form.get('players')
        nome_personagem = request.form['nome']
        return redirect(url_for('dados', nome = nome_personagem, genero = player))

    return render_template('index.html',
        title='Página Inicial',
    )

@app.route('/Dados/<nome><genero>', methods = ['POST', 'GET'])
def dados(nome, genero):
    print(genero)
    salario = None
    if genero == '1' or genero == '2':
        salario = dd.income_gender()
        salario = salario.iat[0,0]
        genero = "Homem"

    elif (genero == '3' or genero == '4'):
        salario = dd.income_gender()
        salario = salario.iat[1,0]
        genero = "Mulher"

    return render_template('dados.html',
        title='Ficha',
        nome = nome,
        genero = genero,
        salario = salario,
    )

if __name__ == '__main__':
    app.run(debug=True)
