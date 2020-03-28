# forms for profile editing and posts

from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import User

# Search Form
class SearchForm(FlaskForm):
  q = StringField('Search', validators=[DataRequired()])

  def __init__(self, *args, **kwargs):
    if 'formdata' not in kwargs:
      kwargs['formdata'] = request.args
    if 'csrf_enabled' not in kwargs:
      kwargs['csrf_enabled'] = False
    super(SearchForm, self).__init__(*args, **kwargs)

# Profile editing form
class EditProfileForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
  submit = SubmitField('Submit')

  def __init__(self, original_username, *args, **kwargs):
    super(EditProfileForm, self).__init__(*args, **kwargs)
    self.original_username = original_username

  def validate_username(self, username):
    if username.data != self.original_username:
      user = User.query.filter_by(username=self.username.data).first()
      if user is not None:
        raise ValidationError('Please use a different username.')

# Post creation form
class PostForm(FlaskForm):
  post = TextAreaField('Say something', validators=[DataRequired()])
  submit = SubmitField('Submit')