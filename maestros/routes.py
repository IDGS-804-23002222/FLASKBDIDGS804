from . import maestros

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from maestros.routes import maestros
from flask_migrate import Migrate #referencia de migrate
from models import Alumnos, Maestros

# todo lo referente a la carpeta de maestros empieza con 'maestros' segun lo definido en el modulo con blueprint
@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"

@maestros.route('/maestros', methods=['GET','POST'])
@maestros.route('/index')
def index():
    create_form = forms.UserForm(request.form)
    maestros = Maestros.query.all()
      
    return render_template('maestros/listadoMaes.html', form=create_form, maestros=maestros)
