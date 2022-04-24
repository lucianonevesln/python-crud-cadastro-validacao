from flask import Flask, render_template, request, jsonify
from flaskext.mysql import MySQL
import config


mysql = MySQL()


app = Flask(__name__)


app.config['MYSQL_DATABASE_DB'] = config.DB
app.config['MYSQL_DATABASE_USER'] = config.USER
app.config['MYSQL_DATABASE_PASSWORD'] = config.PASS
app.config['MYSQL_DATABASE_HOST'] = config.DB_URL


mysql.init_app(app)


def cadastrar_insere_valores(nome, cpf, email, telefone):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
                   f'insert into projetos.cadastros (nome, \
                     cpf, email, telefone) values ("{nome}",\
                     "{cpf}", "{email}", "{telefone}");'
                   )
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('cadastrar.html')


def consultar_cadastros_inseridos():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
                   'select * from projetos.cadastros;'
                   )
    cadastros = cursor.fetchall()
    conn.commit()
    return jsonify(cadastros)
    cursor.close()
    conn.close()


def alterar_nome_insere_valores(cpf, nome):
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute(
                 f'update projetos.cadastros\
                   set nome = "{nome}"\
                   where cpf = "{cpf}";'
                 )
  conn.commit()
  cursor.close()
  conn.close()
  return render_template('alterar_nome.html')


def alterar_email_insere_valores(cpf, email):
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute(
                 f'update projetos.cadastros\
                   set email = "{email}"\
                   where cpf = "{cpf}";'
                 )
  conn.commit()
  cursor.close()
  conn.close()
  return render_template('alterar_email.html')


def alterar_telefone_insere_valores(cpf, telefone):
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute(
                 f'update projetos.cadastros\
                   set telefone = "{telefone}"\
                   where cpf = "{cpf}";'
                 )
  conn.commit()
  cursor.close()
  conn.close()
  return render_template('alterar_telefone.html')


def deletar_cadastro(cpf):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(
                   f'delete from projetos.cadastros\
                     where cpf = "{cpf}";'
                   )
    conn.commit()
    cursor.close()
    conn.close()
    return render_template('deletar.html')