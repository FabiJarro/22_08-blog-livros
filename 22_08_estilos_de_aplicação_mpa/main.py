from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')

@app.route("/resenhaspopulares")
def resenhaspopulares():
    return render_template('resenhaspopulares.html')

@app.route("/lancamentos")
def lancamentos():
    return render_template('lancamentos.html')

@app.route("/noticiasdestaques")
def noticiasdestaques():
    return render_template('noticiasdestaques.html')

@app.route("/resenhacincopassos")
def resenhacincopassos():
    return render_template('resenhas.html')

@app.route("/materianoticia")
def materianoticia():
    return render_template('materianoticia.html')


















if __name__=='__main__':
    app.run(debug=True)
    