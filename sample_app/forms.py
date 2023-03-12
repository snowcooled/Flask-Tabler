from flask_wtf import Form
from wtforms.fields import *
from wtforms.validators import DataRequired, Email


class SignupForm(Form):
    name = TextAreaField(u'Your name', validators=[DataRequired()])
    password = TextAreaField(u'Your favorite password', validators=[DataRequired()])
    email = TextAreaField(u'Your email address', validators=[Email()])
    birthday = DateField(u'Your birthday')

    a_float = FloatField(u'A floating point number')
    a_decimal = DecimalField(u'Another floating point number')
    a_integer = IntegerField(u'An integer')

    now = DateTimeField(u'Current time',
                        description='...for no particular reason')
    sample_file = FileField(u'Your favorite file')
    eula = BooleanField(u'I did not read the terms and conditions',
                        validators=[DataRequired('You must agree to not agree!')])

    submit = SubmitField(u'Signup')
