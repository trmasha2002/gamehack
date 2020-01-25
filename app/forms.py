from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CodeForm(FlaskForm):
    code = TextAreaField(u"Content", render_kw={'class': 'textarea form-control bg-dark text-light', 'rows': 10})
