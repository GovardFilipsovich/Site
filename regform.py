from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class RegForm(FlaskForm):
    username = StringField('Введите логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_check = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрировать')
