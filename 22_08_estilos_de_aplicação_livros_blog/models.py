from db import db 

class Usuario(db.Model):
    __tablename__='usuarios'

    id=db.Column(db.Integer, primary_key=True) 

    nome=db.Column(db.String(30),nullable=False, unique=True)
    senha: db.Column(db.String())

