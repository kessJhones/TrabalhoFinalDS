from flask import Flask, redirect, url_for, request, render_template
import dados as dd

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html',
        title='Página Inicial',
    )

# Essa rota usa o method 'POST' e NAO MOSTRA OS DADOS NA URL.
@app.route('/Dados/', methods=['POST','GET'])
def dados():
    if request.method == 'POST':
        nome_personagem = request.form['nome']
        genero = request.form.get('players')
        idade = request.form.get('idade')
        estado =  request.form.get('estado')

    players = {'blue':('Mulher','Branca','blue'), 'green':('Mulher','Negra','green'),
                'grey':('Homem','Branco','grey'), 'red':('Homem','Negro','red')}

    (genero, raça, cor) = players.get(genero, ('','',''))

    if genero == 'Mulher':
        if raça == 'Branca':
            salario = dd.income_gender()
            salario = salario.iat[1,0]
        elif raça == 'Negra':
            salario = dd.income_gender()
            salario = salario.iat[1,0]
    
    if genero == 'Homem':
        if raça == 'Branco':
            salario = dd.income_gender()
            salario = salario.iat[0,0]
        elif raça == 'Negro':
            salario = dd.income_gender()
            salario = salario.iat[0,0]
    
    return render_template('dados.html',
        title='Ficha',
        nome = nome_personagem,
        idade = idade,
        genero = genero,
        raça = raça,
        salario = salario,
        estado = estado,
        cor = cor,
    )

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True)
