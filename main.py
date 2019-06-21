from flask import Flask, redirect, url_for, escape, request, render_template, flash
import dados as dd

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        nome_personagem = request.form['nome']
        player = request.form.get('players')
        idade = request.form.get('idade')
        estado =  request.form.get('estado')
        return redirect(url_for('dados', nome = nome_personagem, genero = player, idade = idade, estado = estado))

    return render_template('index.html',
        title='Página Inicial',
    )

@app.route('/Dados/<nome>-<genero>-<idade>-<estado>', methods = ['POST', 'GET'])
def dados(nome, genero, idade, estado):
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
        idade = idade,
        genero = genero,
        salario = salario,
        estado = estado,
    )

if __name__ == '__main__':
    app.run(debug=True)
