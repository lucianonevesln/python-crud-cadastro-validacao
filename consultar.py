from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
import config


mysql = MySQL()


app = Flask(__name__)


app.config['MYSQL_DATABASE_DB'] = config.DB
app.config['MYSQL_DATABASE_USER'] = config.USER
app.config['MYSQL_DATABASE_PASSWORD'] = config.PASS
app.config['MYSQL_DATABASE_HOST'] = config.DB_URL


mysql.init_app(app)


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