from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()
class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.Integer, unique=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(200))
    correo = db.Column(db.String(120))
    telefono = db.Column(db.String(10))
    create_date = db.Column(db.DateTime,
                            default=datetime.datetime.now)
   
class Maestros(db.Model):
    __tablename__ = 'maestros'
    id = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.Integer, unique=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    especialidad = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    cursos = db.relationship('Curso', back_populates='maestro')
 