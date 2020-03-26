# setup for error handlers

from flask import render_template
from app import db
from app.errors import bp

# 404 Not Found
@bp.app_errorhandler(404)
def not_found_error(error):
  return render_template('errors/404.html'), 404

# 500 Internal Server Error
@bp.app_errorhandler(500)
def internal_error(error):
  db.session.rollback()
  return render_template('errors/500.html'), 500