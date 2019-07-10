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
        escolaridade = request.form.get('escolaridade')
        estado =  request.form.get('estado')

    personagens = {'blue':('Mulher','Branca','blue'), 'green':('Mulher','Negra','green'),
               'grey':('Homem','Branco','grey'), 'red':('Homem','Negro','red')}
    raça_dataframe = {'Branca':'B', 'Branco':'B', 'Negro':'N', 'Negra':'N'}

    (genero, raça, cor) = personagens.get(genero, ('','',''))

    raça_dataframe = raça_dataframe.get(raça, '')
    salario = dd.income(genero, raça_dataframe, estado, escolaridade)
    
    return render_template('dados.html',
        title='Ficha',
        nome = nome_personagem,
        idade = idade,
        genero = genero,
        raça = raça,
        salario = salario,
        escolaridade = escolaridade,
        estado = estado,
        cor = cor,
    )

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True)
