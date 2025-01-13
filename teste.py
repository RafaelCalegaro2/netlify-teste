from flask import Flask, request, render_template

# cria a instância principal do flask
app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def home():
    return render_template("treino.html") # Renderiza o arquivo html da pasta 'templates'

# cria uma rota (endpoint) chamada 'submit' e define o método de comunicação como POST(mais seguro)
@app.route('/submit', methods=['POST'])

def pegar_form():
    nome = request.form['Nome'] # Captura o campo 'Nome' do formulário
    return f"Nome Cadastrado: {nome}"  # Retorna uma resposta simples com o nome recebido

# Verifica se o arquivo está sendo executado diretamente (e não importado como módulo)
if __name__== "__main__":
    # faz o flask rodar com depurador ativado
    app.run(host='0.0.0.0', debug=False)