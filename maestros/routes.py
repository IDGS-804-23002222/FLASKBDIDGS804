from . import maestros

from flask import Flask, render_template, request, redirect, url_for, flash
import forms
from models import Maestros, Alumnos, Cursos, db
# todo lo referente a la carpeta de maestros empieza con 'maestros' segun lo definido en el modulo con blueprint

@maestros.route('/')
def index():
    form = forms.MaestrosForm(request.form)
    maestros = Maestros.query.all()
      
    return render_template('maestros/listadoMaes.html', form=form, maestros=maestros)

@maestros.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = forms.MaestrosForm(request.form)

    if request.method == "POST" and form.validate():
        
        maestro_existente = Maestros.query.filter.by(matricula=form.matricula.data).first()
        
        if maestro_existente:
            flash("La matrícula ya está registrada.", "danger")
            return render_template("maestros/registrar.html", form=form)

        maes = Maestros(
            matricula=form.matricula.data,
            nombre=form.nombre.data,
            apellido=form.apellido.data,
            especialidad=form.especialidad.data,
            correo=form.correo.data
        )
        
        db.session.add(maes)
        db.session.commit()
        
        flash('¡Maestro registrado exitosamente!', 'success')
        return redirect(url_for("maestros.index"))

    return render_template("maestros/registrar.html", form=form)

@maestros.route("/detalles", methods=["GET", "POST"])
def detalles():
    if request.method == "GET":
        id = request.args.get("id")
        maes1 = db.session.query(Maestros).filter(Maestros.id == id).first()

        matricula = maes1.matricula
        nombre = maes1.nombre
        apellido = maes1.apellido
        especialidad = maes1.especialidad
        correo = maes1.correo
        
    return render_template("maestros/detalles.html", matricula=matricula, nombre=nombre, apellido=apellido, especialidad=especialidad, correo=correo)

@maestros.route("/modificar", methods=["GET", "POST"])
def modificar():
    form = forms.MaestrosForm(request.form)
    id = request.args.get("id")
    maes1 = db.session.query(Maestros).filter(Maestros.id == id).first()
    if request.method == "GET":
        form.matricula.data=maes1.matricula
        form.nombre.data = maes1.nombre
        form.apellido.data = maes1.apellido
        form.especialidad.data = maes1.especialidad
        form.correo.data=maes1.correo

    if request.method == "POST":
        maes1.id=id
        maes1.matricula=form.matricula.data
        maes1.nombre=form.nombre.data
        maes1.apellido=form.apellido.data
        maes1.especialidad=form.especialidad.data
        maes1.correo=form.correo.data
        db.session.add(maes1)
        db.session.commit()
        flash('¡Maestro modificado exitosamente!', 'success')
        return redirect(url_for("maestros.index"))

    return render_template("maestros/modificar.html", form=form)

@maestros.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    form = forms.MaestrosForm(request.form)
    id = request.args.get("id")
    maes1 = db.session.query(Maestros).filter(Maestros.id == id).first()
    if request.method == "GET":
        form.matricula.data=maes1.matricula
        form.nombre.data = maes1.nombre
        form.apellido.data = maes1.apellido
        form.especialidad.data = maes1.especialidad
        form.correo.data=maes1.correo

    if request.method == "POST":
        db.session.delete(maes1)
        db.session.commit()
        flash('¡Maestro eliminado exitosamente!', 'success')
        return redirect(url_for("maestros.index"))

    return render_template("maestros/eliminar.html", form=form)