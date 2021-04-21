from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from data.users import User
from data import db_session


class RegForm(FlaskForm):
    username = StringField('Введите логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_check = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрировать')

    def check_password(self):
        if self.password.data == self.password_check.data:
            return True

    def check_user(self):
        db_sess = db_session.create_session()
        return db_sess.query(User).filter(User.name == self.username.data).first()