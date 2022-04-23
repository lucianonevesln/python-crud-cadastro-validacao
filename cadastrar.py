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