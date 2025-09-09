from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']="mysql://username:password@server/db"

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:aham@localhost/db"


db=SQLAlchemy()
db.init_app(app)


class Usuario(db.Model):
    __tablename__='usuarios'
    id=db.Column(db.Integer, primary_key=True) 
    nome=db.Column(db.String(40),nullable=False, unique=True)






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




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        user_existente = Usuario.query.filter_by(nome="Lan").first()
        if not user_existente:
            user = Usuario(nome="Lan")
            db.session.add(user)
            db.session.commit()
            db.drop_all()
            db.create_all()

        
        
        

    app.run(debug=True)
    