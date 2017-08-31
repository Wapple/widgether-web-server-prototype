from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, EqualTo

def strip_filter(x):
    if isinstance(x, str):
        return x.strip()
    else:
        return x

class LoginForm(FlaskForm):
    user_id = StringField('사용자 아이디', filters=[strip_filter],
        validators=[DataRequired()])
    user_pw = PasswordField('사용자 비밀번호', filters=[strip_filter],
        validators=[DataRequired()])

class RegisterForm(FlaskForm):
    user_id = StringField('사용자 아이디', filters=[strip_filter],
        validators=[DataRequired()])
    user_name = StringField('사용자 이름', filters=[strip_filter],
        validators=[DataRequired()])
    user_pw = PasswordField('사용자 비밀번호', filters=[strip_filter],
        validators=[DataRequired(), EqualTo('user_pw')])
    user_pw_confirm = PasswordField('비밀번호 확인', filters=[strip_filter],
        validators=[DataRequired(), EqualTo('user_pw')])
    user_type = SelectField('사용자 타입',
        choices=[('normal', '일반'), ('developer', '개발자')],
        default='normal', filters=[strip_filter], validators=[DataRequired()])