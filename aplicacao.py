from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route("/historia.html")
def historia():
    return render_template("historia.html")

@app.route("/copa.html")   
def copa():
    return render_template("copa.html")

@app.route("/jogadores.html")
def jogadores():
    return render_template("jogadores.html")

@app.route("/noticia.html")
def noticia():
    return render_template("noticia.html")

app.run()


#"http://127.0.0.1:5000/home" #enderco URL

#localhost:5000/home  # outro caminho q da pra por de URL
