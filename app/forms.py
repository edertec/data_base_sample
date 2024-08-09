from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired

class ClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Registrar Cliente')

class IngressoForm(FlaskForm):
    evento = StringField('Evento', validators=[DataRequired()])
    preco = FloatField('Preço', validators=[DataRequired()])
    submit = SubmitField('Registrar Ingresso')

class CompraForm(FlaskForm):
    cliente_id = SelectField('Cliente', coerce=int, validators=[DataRequired()])
    ingresso_id = SelectField('Evento', coerce=int, validators=[DataRequired()])
    quantidade = IntegerField('Quantidade', validators=[DataRequired()])
    submit = SubmitField('Registrar Compra')
