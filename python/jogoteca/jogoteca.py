from flask import Flask, flash, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "alura" 

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogos = [
    Jogo("Tetris", "Puzzle", "Game Boy"),
    Jogo("Super Mario", "Plataforma", "Super Nintendo"),
    Jogo("Paciência", "Cartas", "Windows"),
    Jogo("Minecraft", "Sandbox", "Multiplataforma"),
    Jogo("Final Fantasy", "RPG", "PlayStation")
]

@app.route("/")
def index():  
    return render_template("lista.html", titulo="Jogos", jogos=jogos)


@app.route("/novo")
def novo_jogo():
    if "usuario_logado" not in session or session["usuario_logado"] == None:
        return redirect(url_for("login", proxima=url_for("novo_jogo")))
    return render_template("novo.html", titulo="Novo Jogo")

@app.route("/criar", methods=["POST"])
def criar_jogo():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    console = request.form["console"]
    novo_jogo = Jogo(nome, categoria, console)

    print(f"Jogo criado: {novo_jogo.nome}, Categoria: {novo_jogo.categoria}, Console: {novo_jogo.console}")
    jogos.append(novo_jogo)

    return redirect(url_for("index"))


@app.route("/login")
def login():
    proxima  = request.args.get("proxima")
    return render_template("login.html", titulo="Login", proxima=proxima)

@app.route("/autenticar", methods=["POST"])
def autenticar():
    usuario = request.form["usuario"]
    senha = request.form["senha"]

    if senha == "alohomora":
        session["usuario_logado"] = usuario
        flash(session["usuario_logado"] + " logado com sucesso!")
        proxima_pagina = request.form["proxima"]
        if proxima_pagina:
            return redirect(proxima_pagina)
        return redirect(url_for("index"))
    else:
        flash("Usuário não logado!")
        redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    usuario = session["usuario_logado"]
    session.pop("usuario_logado", None)
    flash(usuario + " deslogado com sucesso!")
    return redirect(url_for("index"))

app.run(debug=True)