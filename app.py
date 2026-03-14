from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate #referencia de migrate
from flask import g
import forms
from models import db, Alumnos, Maestros, Cursos
from maestros.routes import maestros
from alumnos.routes import alumnos
from cursos.routes import cursos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros, url_prefix="/maestros") #registrar el blueprint de maestros
app.register_blueprint(alumnos, url_prefix="/alumnos")
app.register_blueprint(cursos, url_prefix="/cursos")
db.init_app(app)
migrate=Migrate(app, db) #migracion a db
#csrf = CSRFProtect()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'),404
    
if __name__ == '__main__':
    #csrf.init_app(app)
    #db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
    
    # flask db init 
    
    #flask db migrate -m 'Crear tabla alumnos'
    
    #por cada cambio a la base de datos se debe hacer upgrade
    #flask db upgrade
    
    #flask db migrate -m 'tabla alumnos con cambios'
    
    
    #para la tarea tambien agregar el nuevo respaldo de la base de datos final