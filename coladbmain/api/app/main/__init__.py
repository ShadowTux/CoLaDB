# init for main scripts

from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes