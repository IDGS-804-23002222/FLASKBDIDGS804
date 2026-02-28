from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate #referencia de migrate
from flask import g
import forms
from models import db, Alumnos
from maestros.routes import maestros
#from alumnos.routes import alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros) #registrar el blueprint de maestros
# app.register blueprint(alumnos)
db.init_app(app)
migrate=Migrate(app, db) #migracion a db
#csrf = CSRFProtect()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    create_form = forms.UserForm(request.form)
    #tem= Alumnos.query('select * from alumnos')
    alumno = Alumnos.query.all()
      
    return render_template('index.html', form=create_form, alumno=alumno)

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos_view():
    create_form = forms.UserForm(request.form)

    if request.method == "POST" and create_form.validate():
        alum = Alumnos(
            matricula=create_form.matricula.data,
            nombre=create_form.nombre.data,
            apellido=create_form.apellido.data,
            correo=create_form.correo.data,
            telefono=create_form.telefono.data
        )
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("alumnos.html", form=create_form)

@app.route("/detalles", methods=["GET", "POST"])
def detalles():
    create_form = forms.UserForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        #select * from alumnos where id==id
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        id = request.args.get("id")
        nombre = alum1.nombre
        apellido = alum1.apellido
        correo = alum1.correo
        matricula=alum1.matricula
        telefono=alum1.telefono

    return render_template("detalles.html", nombre=nombre, apellido=apellido, correo=correo, matricula=matricula, telefono=telefono)

@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.UserForm(request.form)
    id = request.args.get("id")
    alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
    if request.method == "GET":
        create_form.nombre.data = alum1.nombre
        create_form.apellido.data = alum1.apellido
        create_form.correo.data = alum1.correo
        create_form.matricula.data=alum1.matricula
        create_form.telefono.data=alum1.telefono

    if request.method == "POST":
        alum1.id=id
        alum1.nombre=create_form.nombre.data
        alum1.apellido=create_form.apellido.data
        alum1.correo=create_form.correo.data
        alum1.matricula=create_form.matricula.data
        alum1.telefono=create_form.telefono.data
        db.session.add(alum1)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("modificar.html", form=create_form)

@app.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.UserForm(request.form)
    id = request.args.get("id")
    alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
    if request.method == "GET":
        create_form.nombre.data = alum1.nombre
        create_form.apellido.data = alum1.apellido
        create_form.correo.data = alum1.correo
        create_form.matricula.data=alum1.matricula
        create_form.telefono.data=alum1.telefono

    if request.method == "POST":
        db.session.delete(alum1)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("eliminar.html", form=create_form)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'),404
    
if __name__ == '__main__':
    #csrf.init_app(app)
    #db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
    #flask db migrate -m 'Crear tabla alumnos'
    
    #por cada cambio a la base de datos se debe hacer upgrade
    #flask db upgrade
    
    #flask db migrate -m 'tabla alumnos con cambios'