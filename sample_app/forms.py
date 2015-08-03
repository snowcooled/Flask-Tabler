from flask_wtf import Form
from wtforms.fields import (TextField, SubmitField, BooleanField, DateField,
                            DateTimeField)
from wtforms.validators import Required, Email


class SignupForm(Form):
    name = TextField(u'Your name', validators=[Required()])
    email = TextField(u'Your email address', validators=[Email()])
    birthday = DateField(u'Your birthday')
    now = DateTimeField(u'Current time',
                        description='...for no particular reason')
    eula = BooleanField(u'I did not read the terms and conditions',
                        validators=[Required('You must agree to not agree!')])
    submit = SubmitField(u'Signup')
