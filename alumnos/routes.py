from . import alumnos

from flask import Flask, render_template, request, redirect, url_for, flash
import forms
from models import Alumnos, Maestros, Cursos, db

@alumnos.route('/')
def index():
    form = forms.AlumnosForm(request.form)
    alumnos = Alumnos.query.all()
      
    return render_template('alumnos/listadoAlum.html', form=form, alumnos=alumnos)

@alumnos.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = forms.AlumnosForm(request.form)

    if request.method == "POST" and form.validate():

        alumno_existente = Alumnos.query.filter_by(matricula=form.matricula.data).first()

        if alumno_existente:
            flash("La matrícula ya está registrada.", "danger")
            return render_template("alumnos/registrar.html", form=form)

        alum = Alumnos(
            matricula=form.matricula.data,
            nombre=form.nombre.data,
            apellido=form.apellido.data,
            correo=form.correo.data,
            telefono=form.telefono.data
        )

        db.session.add(alum)
        db.session.commit()

        flash('¡Alumno registrado exitosamente!', 'success')
        return redirect(url_for("alumnos.index"))

    return render_template("alumnos/registrar.html", form=form)

@alumnos.route("/detalles", methods=["GET", "POST"])
def detalles():
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

    return render_template("alumnos/detalles.html", nombre=nombre, apellido=apellido, correo=correo, matricula=matricula, telefono=telefono)

@alumnos.route("/modificar", methods=["GET", "POST"])
def modificar():
    create_form = forms.AlumnosForm(request.form)
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
        flash('¡Alumno modificado exitosamente!', 'success')
        return redirect(url_for("alumnos.index"))

    return render_template("alumnos/modificar.html", form=create_form)

@alumnos.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    create_form = forms.AlumnosForm(request.form)
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
        flash('Registro eliminado correctamente', 'warning')
        return redirect(url_for("alumnos.index"))

    return render_template("alumnos/eliminar.html", form=create_form)
