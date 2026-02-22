from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "alura" 

app.config['SQLALCHEMY_DATABASE_URI'] = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = '12345678',
    servidor = 'localhost', 
    database = 'jogoteca'
)
db = SQLAlchemy(app) 

app.run(debug=True)