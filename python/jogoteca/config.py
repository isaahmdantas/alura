
SECRET_KEY = "alura" 

SQLALCHEMY_DATABASE_URI: str = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = '123456',
    servidor = 'localhost', 
    database = 'jogoteca'
)