from wtforms import Form, StringField, IntegerField, EmailField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, Email


class AlumnosForm(Form):

    matricula = IntegerField(
        "Matrícula",
        [
            DataRequired(message="La matrícula es obligatoria")
        ]
    )

    nombre = StringField(
        "Nombre",
        [
            DataRequired(message="El nombre es obligatorio"),
            Length(min=2, max=50, message="El nombre debe tener entre 2 y 50 caracteres")
        ]
    )

    apellido = StringField(
        "Apellido",
        [
            DataRequired(message="El apellido es obligatorio"),
            Length(min=2, max=50, message="El apellido debe tener entre 2 y 50 caracteres")
        ]
    )

    correo = EmailField(
        "Correo",
        [
            DataRequired(message="El correo es obligatorio"),
            Email(message="Ingrese un correo válido")
        ]
    )
    
    telefono = StringField(
        "Telefono",
        [
            DataRequired(message="El telefono es obligatorio")
        ]
    )
    
class MaestrosForm(Form):
    matricula = IntegerField(
        "Matrícula",
        [
            DataRequired(message="La matrícula es obligatoria")
        ]
    )

    nombre = StringField(
        "Nombre",
        [
            DataRequired(message="El nombre es obligatorio"),
            Length(min=2, max=50, message="El nombre debe tener entre 2 y 50 caracteres")
        ]
    )

    apellido = StringField(
        "Apellido",
        [
            DataRequired(message="El apellido es obligatorio"),
            Length(min=2, max=50, message="El apellido debe tener entre 2 y 50 caracteres")
        ]
    )

    correo = EmailField(
        "Correo",
        [
            DataRequired(message="El correo es obligatorio"),
            Email(message="Ingrese un correo válido")
        ]
    )
     
    especialidad = StringField(
        "Especialidad",
        [
            DataRequired(message="La especialidad es obligatoria")
        ]
    )
    
class CursosForm(Form):
    nombre = StringField(
        "Nombre",
        [
            DataRequired(message="El nombre es obligatorio"),
            Length(min=2, max=150, message="El nombre debe tener entre 2 y 150 caracteres")
        ]
    )

    descripcion = StringField(
        "Descripción",
        [
            DataRequired(message="La descripción es obligatoria")
        ]
    )
    
    maestro_id = SelectField(
        "Maestro",
        coerce=int,
        validators=[
            DataRequired(message="El maestro es obligatorio")
        ]
    )