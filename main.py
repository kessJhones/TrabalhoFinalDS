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


    if genero == 'Homem':
        if raça == 'Branco':
            info = "Seu personagem recebe 100% das moedas coletadas." 
        elif raça == 'Negro':
            info = "Seu personagem recebe apenas 70% das moedas coletadas."
    elif genero == 'Mulher':
        if raça == 'Negra':
            info = "Seu personagem recebe apenas 50% das moedas coletadas."
        elif raça == 'Branca':
            info = "Seu personagem recebe apenas 80% das moedas coletadas."
    
    if salario >= dd.income_mean_uf(estado):
       media_salario_uf = "acima da média do seu estado."
    else:
       media_salario_uf = "abaixo da média do seu estado."
    if salario >= dd.income_mean():
        media_salario = "Seu salario está acima da média nacional e {}".format(media_salario_uf)
    else:
        media_salario = "Seu salario está abaixo da média nacional e {}".format(media_salario_uf)

    
    media_escolaridade = "PLACEHOLDER Vantagem!"

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
        info = info,
        media_salario = media_salario,
        media_escolaridade = media_escolaridade,
    )

if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=True)
