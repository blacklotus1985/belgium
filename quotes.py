from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:62662@localhost/quotes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#instance of sqlalchemy
db = SQLAlchemy(app)
class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    text = db.Column(db.String(2000))

class Letters(db.Model):
    id_lettera = db.Column(db.Integer,primary_key=True)
    mittente = db.Column(db.String(50))
    destinatario = db.Column(db.String(50))
    luogo_di_spedizione = db.Column(db.String(50))
    data_di_spedizione = db.Column(db.Date)
    luoghi_menzionati = db.Column(db.String(500))
    personaggi_menzionati = db.Column(db.String(500))
    fondo = db.Column(db.String(200))
    numerazione_pagine = db.Column(db.Integer)
    numero_prima_carta = db.Column(db.Integer)
    facciata_prima_carta = db.Column(db.Enum('r','v',name='types_of_pages'))
    numero_totale_facciate = db.Column(db.Integer)
    tipologia_lettera = db.Column(db.Integer)
    presenza_nota_ricezione = db.Column(db.Boolean)
    nota_di_ricezione = db.Column(db.String(100))
    presenza_indirizzo = db.Column(db.Boolean)
    indirizzo = db.Column(db.String(100))
    presenza_filigrana = db.Column(db.Boolean)
    presenza_sigillo = db.Column(db.Boolean)
    presenza_firma = db.Column(db.Boolean)
    firma = db.Column(db.String(50))
    dimensione = db.Column(db.String(15))
    formula_di_saluto = db.Column(db.String(100))
    testo = db.Column(db.Text)
    notes = db.Column(db.Text)

db.create_all()




















@app.route('/')
def index():
    return '<h1> Hello World </h1>'

@app.route('/about')
def about():
    return '<h1> Hello World from about </h1>'

@app.route('/quotes')
def quotes():
    return 'Love from the common people'