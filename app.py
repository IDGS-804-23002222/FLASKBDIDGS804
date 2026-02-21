from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from models import db, Alumnos


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
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
            correo=create_form.correo.data
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

        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        id = request.args.get("id")
        nombre = alum1.nombre
        apellido = alum1.apellido
        correo = alum1.correo

    return render_template("detalles.html", nombre=nombre, apellido=apellido, correo=correo)


@app.errorhandler(404)
def not_found():
    return render_template('404.html'),404
    
if __name__ == '__main__':
    #csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
    #Lista de alumnos y fecha