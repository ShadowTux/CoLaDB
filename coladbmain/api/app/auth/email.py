# mail functions for auth

from flask import render_template, current_app
from app.email import send_email

# password reset
def send_password_reset_email(user):
  token = user.get_reset_password_token()
  send_email('[CoLaDB] Reset Your Password',
    sender=app.config['ADMINS'][0],
    recipients=[user.email],
    text_body=render_template('email/reset_password.txt', user=user, token=token),
    html_body=render_template('email/reset_password.html', user=user, token=token))