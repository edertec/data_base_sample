from . import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    compras = db.relationship('Compra', backref='cliente', lazy=True)  # Backref definido aqui

class Ingresso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    evento = db.Column(db.String(150), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    compras = db.relationship('Compra', backref='ingresso', lazy=True)  # Backref definido aqui

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    ingresso_id = db.Column(db.Integer, db.ForeignKey('ingresso.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
