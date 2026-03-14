from . import cursos

from flask import Flask, render_template, request, redirect, url_for, flash
import forms
from models import Cursos, Maestros, Alumnos, db

@cursos.route('/')
def index():
    form = forms.CursosForm(request.form)
    cursos = Cursos.query.all()
      
    return render_template('cursos/listadoCurs.html', form=form, cursos=cursos)

@cursos.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = forms.CursosForm(request.form)
    
    maestros = Maestros.query.all()
    form.maestro_id.choices = [
        (m.id, f"{m.nombre} {m.apellido}") for m in maestros
        ]
    

    if request.method == "POST" and form.validate():
        curs = Cursos(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            maestro_id=form.maestro_id.data
        )
        db.session.add(curs)
        db.session.commit()
        flash('¡Curso registrado exitosamente!', 'success')
        return redirect(url_for("cursos.index"))

    return render_template("cursos/registrar.html", form=form, maestros=maestros)

@cursos.route('/inscritos/<int:curso_id>')
def inscritos(curso_id):
    curso = Cursos.query.get_or_404(curso_id)
    alumnos = curso.alumnos

    # Alumnos que pueden ser inscritos (no están ya inscritos en el curso)
    disponibles = Alumnos.query.filter(
        ~Alumnos.cursos.any(id=curso_id)
    ).all()

    return render_template(
        "cursos/inscritos.html",
        curso=curso,
        alumnos=alumnos,
        disponibles=disponibles
    )

@cursos.route('/listadoInscritos')
def listadoInscritos():

    alumno_id = request.args.get("alumno_id")
    maestro_id = request.args.get("maestro_id")
    curso_id = request.args.get("curso_id")

    query = Cursos.query

    # filtro por docente
    if maestro_id:
        query = query.filter(Cursos.maestro_id == maestro_id)

    # filtro por curso
    if curso_id:
        query = query.filter(Cursos.id == curso_id)

    # filtro por alumno
    if alumno_id:
        query = query.join(Cursos.alumnos).filter(Alumnos.id == alumno_id)

    cursos = query.all()

    alumnos_all = Alumnos.query.all()
    maestros = Maestros.query.all()
    cursos_all = Cursos.query.all()

    return render_template(
        'cursos/listadoInscritos.html',
        cursos=cursos,
        alumnos_all=alumnos_all,
        maestros=maestros,
        cursos_all=cursos_all
    )

@cursos.route("/filtrar", methods=["GET"])
def filtrar():

    alumno_id = request.args.get("alumno_id")
    maestro_id = request.args.get("maestro_id")
    curso_id = request.args.get("curso_id")

    cursos = []
    alumnos = []
    maestros = Maestros.query.all()

    if alumno_id:
        alumno = Alumnos.query.get(alumno_id)
        cursos = alumno.cursos

    elif maestro_id:
        cursos = Cursos.query.filter_by(maestro_id=maestro_id).all()

    elif curso_id:
        curso = Cursos.query.get(curso_id)
        alumnos = curso.alumnos
        cursos = [curso]

    alumnos_all = Alumnos.query.all()
    cursos_all = Cursos.query.all()

    return render_template(
        "cursos/listadoInscritos.html",
        cursos=cursos,
        alumnos=alumnos,
        maestros=maestros,
        alumnos_all=alumnos_all,
        cursos_all=cursos_all
    )
    
@cursos.route("/inscribir", methods=["POST"])
def inscribir():
    alumno_id = request.form.get("alumno_id")
    curso_id = request.form.get("curso_id")

    curso = Cursos.query.get_or_404(curso_id)
    alumno = Alumnos.query.get_or_404(alumno_id)

    if alumno not in curso.alumnos:
        curso.alumnos.append(alumno)
        db.session.commit()
        flash("Alumno inscrito correctamente.", "success")
    else:
        flash("El alumno ya está inscrito.", "warning")

    return redirect(url_for("cursos.inscritos", curso_id=curso_id))

@cursos.route("/desinscribir", methods=["POST"])
def desinscribir():

    alumno_id = request.form.get("alumno_id")
    curso_id = request.form.get("curso_id")

    curso = Cursos.query.get_or_404(curso_id)
    alumno = Alumnos.query.get_or_404(alumno_id)

    curso.alumnos.remove(alumno)
    db.session.commit()

    flash("Alumno eliminado del curso.", "success")

    return redirect(url_for("cursos.inscritos", curso_id=curso_id))    

@cursos.route("/modificar", methods=["GET", "POST"])
def modificar():
    form = forms.CursosForm(request.form)
    
    maestros = Maestros.query.all()
    form.maestro_id.choices = [
        (m.id, f"{m.nombre} {m.apellido}") for m in maestros
        ]
    
    id = request.args.get("id")
    curs1 = db.session.query(Cursos).filter(Cursos.id == id).first()
    
    if request.method == "GET":
        form.nombre.data = curs1.nombre
        form.descripcion.data = curs1.descripcion
        form.maestro_id.data = curs1.maestro_id

    if request.method == "POST":
        curs1.id=id
        curs1.nombre=form.nombre.data
        curs1.descripcion=form.descripcion.data
        curs1.maestro_id=form.maestro_id.data
        db.session.add(curs1)
        db.session.commit()
        flash('¡Curso modificado exitosamente!', 'success')
        return redirect(url_for("cursos.index"))

    return render_template("cursos/modificar.html", form=form)

@cursos.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    form = forms.CursosForm(request.form)
  
    maestros = Maestros.query.all()
    form.maestro_id.choices = [
        (m.id, f"{m.nombre} {m.apellido}") for m in maestros
        ]
    
    id = request.args.get("id")
    curs1 = db.session.query(Cursos).filter(Cursos.id == id).first()
    if request.method == "GET":
        form.nombre.data = curs1.nombre
        form.descripcion.data = curs1.descripcion
        form.maestro_id.data = curs1.maestro_id

    if request.method == "POST":
        db.session.delete(curs1)
        db.session.commit()
        flash('¡Curso eliminado exitosamente!', 'success')
        return redirect(url_for("cursos.index"))

    return render_template("cursos/eliminar.html", form=form)





