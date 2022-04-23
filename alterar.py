from flask import Flask, render_template
from flaskext.mysql import MySQL
import config


mysql = MySQL()


app = Flask(__name__)


app.config['MYSQL_DATABASE_DB'] = config.DB
app.config['MYSQL_DATABASE_USER'] = config.USER
app.config['MYSQL_DATABASE_PASSWORD'] = config.PASS
app.config['MYSQL_DATABASE_HOST'] = config.DB_URL


mysql.init_app(app)


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