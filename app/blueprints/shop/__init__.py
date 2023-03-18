from flask import Blueprint

shop = Blueprint('shop', __name__, url_prefix='/') #Aquí establecemos la direccion url

from .resources import index #Aquí importamos el recurso