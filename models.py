from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()
class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.Integer, unique=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)