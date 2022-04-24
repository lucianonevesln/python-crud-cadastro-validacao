from flask import Flask, request, render_template
from database import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/cadastrar', methods=['GET'])
def cadastrar():
    return render_template('cadastrar.html')


@app.route('/cadastrar', methods=['POST'])
def cadastrar_recebe_valores():
    nome = request.form['id_nome']
    cpf = request.form['id_cpf']
    email = request.form['id_email']
    telefone = request.form['id_telefone']
    if nome == ''     or\
       cpf == ''      or\
       len(cpf) != 11 or\
       email == ''    or\
       telefone == '' or\
       len(telefone) != 11:
       return {"message":\
               "Verifique se os dados foram inseridos "\
               "corretamente."}
    else:
        return cadastrar_insere_valores(nome, cpf, email, telefone)


@app.route('/consultar-cadastros', methods=['GET'])
def consultar_cadastros():
    return consultar_cadastros_inseridos()


@app.route('/alterar-nome', methods=['GET'])
def alterar_nome():
    return render_template('alterar_nome.html')


@app.route('/alterar-nome', methods=['POST'])
def alterar_nome_recebe_valores():
    cpf = request.form['id_cpf']
    nome = request.form['id_nome_atual']
    if nome == ''     or\
       cpf == ''      or\
       len(cpf) != 11:
       return {"message":\
               "Verifique se os dados foram inseridos "\
               "corretamente."}
    else:
        return alterar_nome_insere_valores(cpf, nome)


@app.route('/alterar-email', methods=['GET'])
def alterar_email():
    return render_template('alterar_email.html')


@app.route('/alterar-email', methods=['POST'])
def alterar_email_recebe_valores():
    cpf = request.form['id_cpf']
    email = request.form['id_email_atual']
    if email == ''     or\
       cpf == ''       or\
       len(cpf) != 11:
       return {"message":\
               "Verifique se os dados foram inseridos "\
               "corretamente."}
    else:
        return alterar_email_insere_valores(cpf, email)


@app.route('/alterar-telefone', methods=['GET'])
def alterar_telefone():
    return render_template('alterar_telefone.html')


@app.route('/alterar-telefone', methods=['POST'])
def alterar_telefone_recebe_valores():
    cpf = request.form['id_cpf']
    telefone = request.form['id_telefone_atual']
    if telefone == ''      or\
       len(telefone) != 11 or\
       cpf == ''           or\
       len(cpf) != 11:
       return {"message":\
               "Verifique se os dados foram inseridos "\
               "corretamente."}
    else:
        return alterar_telefone_insere_valores(cpf, telefone)


@app.route('/deletar', methods=['GET'])
def deletar():
    return render_template('deletar.html')


@app.route('/deletar', methods=['POST'])
def deletar_recebe_valor():
    cpf = request.form['id_cpf']
    if cpf == '' or len(cpf) != 11:
        return {"message":\
                "CPF invalido."}
    else:
        return deletar_cadastro(cpf)


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000, debug = True)