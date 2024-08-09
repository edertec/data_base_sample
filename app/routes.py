from flask import Blueprint, render_template, redirect, url_for
from .forms import ClienteForm, IngressoForm, CompraForm
from .models import Cliente, Ingresso, Compra
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add_cliente', methods=['GET', 'POST'])
def add_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        cliente = Cliente(nome=form.nome.data, email=form.email.data)
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_cliente.html', form=form)

@main.route('/add_ingresso', methods=['GET', 'POST'])
def add_ingresso():
    form = IngressoForm()
    if form.validate_on_submit():
        ingresso = Ingresso(evento=form.evento.data, preco=form.preco.data)
        db.session.add(ingresso)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_ingresso.html', form=form)

@main.route('/add_compra', methods=['GET', 'POST'])
def add_compra():
    form = CompraForm()
    form.cliente_id.choices = [(c.id, c.nome) for c in Cliente.query.order_by('nome')]
    form.ingresso_id.choices = [(i.id, f"{i.evento} (R${i.preco})") for i in Ingresso.query.order_by('evento')]

    if form.validate_on_submit():
        compra = Compra(
            cliente_id=form.cliente_id.data,
            ingresso_id=form.ingresso_id.data,
            quantidade=form.quantidade.data
        )
        db.session.add(compra)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_compra.html', form=form)

@main.route('/listar_compras')
def listar_compras():
    compras = Compra.query.options(db.joinedload(Compra.cliente), db.joinedload(Compra.ingresso)).all()
    return render_template('listar_compras.html', compras=compras)

