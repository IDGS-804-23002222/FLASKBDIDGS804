# nombre para generar un modulo
from flask import Blueprint

cursos =  Blueprint(
    'cursos',
    __name__,
    template_folder = 'templates',
    static_folder = 'static'
)

from . import routes