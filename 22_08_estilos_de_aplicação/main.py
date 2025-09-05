from flask import Flask, render_template
# from models import Usuario
# from db import db



app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI']="mysql://username:password@server/db"

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123@localhost/db"
# db = SQLAlchemy(app)

# db=SQLAlchemy()

# # class Usuário(db.Model):
# #     __tablename__='usuarios'

# #     id=db.Column(db.Integer, primary_key=True) 
# #     nome=db.Column(db.String(40),nullable=False, unique=True)






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
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
    