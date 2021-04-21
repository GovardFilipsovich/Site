from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from data.users import User
from data import db_session
from hashlib import sha256


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

    def is_in_db(self):
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.name.like(self.username.data), User.password.like(sha256(
            self.password.data.encode('utf-8')).hexdigest())).first()
        if user != None:
            return True

    def get_user(self):
        return self.username.data
