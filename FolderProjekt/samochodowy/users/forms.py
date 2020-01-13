from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from samochodowy.models import User

class LoginForm(FlaskForm):
    email = StringField('Email: ',validators=[DataRequired(),Email()])
    password = PasswordField('Hasło: ',validators=[DataRequired()])
    submit = SubmitField('Zaloguj')

class RegistrationForm(FlaskForm):
    email = StringField('Email: ',validators=[DataRequired(),Email()])
    username = StringField('Nazwa użytkownika: ',validators=[DataRequired()])
    password = PasswordField('Hasło: ',validators=[DataRequired(),EqualTo('pass_confirm',message='Haslo musi byc poprawne')])
    pass_confirm = PasswordField('Potwierdz hasło: ',validators=[DataRequired()])
    submit = SubmitField('Zarejestruj')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('bład')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('bład')


class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    picture = FileField('Zaktualizuj zdjecie Profilowe', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Wgraj nowe zdjecie')

    def check_email(self, field):
       
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('bład')

    def check_username(self, field):
        
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('bład')
