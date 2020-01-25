from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class CodeForm(FlaskForm):
    code = StringField()
    submit = SubmitField('Code In')