from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import environ
from sqlalchemy import create_engine




now = datetime.now()
now.strftime("%Y-%m-%d %H:%M:%S")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:62662@localhost/quotes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_uri = environ.get('SQLALCHEMY_DATABASE_URI')
engine = create_engine('postgresql+psycopg2://postgres:62662@localhost/quotes', echo=True)



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
    luogo_di_conservazione = db.Column(db.String(100))
    fondo = db.Column(db.String(200))
    numerazione_pagine = db.Column(db.Integer)
    numero_prima_carta = db.Column(db.Integer)
    facciata_prima_carta = db.Column(db.Enum('r','v',name='types_of_pages'))
    numero_totale_facciate = db.Column(db.Integer)
    tipologia_lettera = db.Column(db.String)
    presenza_nota_ricezione = db.Column(db.Integer)
    nota_di_ricezione = db.Column(db.String(100))
    presenza_indirizzo = db.Column(db.Integer)
    indirizzo = db.Column(db.String(100))
    presenza_filigrana = db.Column(db.Integer)
    presenza_sigillo = db.Column(db.Integer)
    presenza_firma = db.Column(db.Integer)
    firma = db.Column(db.String(50))
    dimensione = db.Column(db.String(15))
    formula_di_saluto = db.Column(db.String(100))
    testo = db.Column(db.Text)
    notes = db.Column(db.Text)
    data_inserimento = db.Column(db.DateTime(now))


db.create_all()
import pandas as pd
df = pd.read_csv(r"C:\Users\black\OneDrive\Desktop\Alex\github_projects\belgium\data\db_postgres.csv",sep=";")
df['data_inserimento'] = now
table_name  = "letters"
df.to_sql(
    table_name,
    engine,
    if_exists='append',
    index=False,
    chunksize=500,
)




















@app.route('/')
def index():
    return '<h1> Hello World </h1>'

@app.route('/about')
def about():
    return '<h1> Hello World from about </h1>'

@app.route('/quotes')
def quotes():
    return 'Love from the common people'