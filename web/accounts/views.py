from flask import Blueprint, redirect, render_template, flash

from flask_login import login_user, logout_user, login_required

from ..utils import redirect_back

from .models import User
from .forms import LoginForm, RegisterForm

accounts_bp = Blueprint('accounts', __name__, template_folder='templates',
    static_folder='static')

@accounts_bp.route('/', methods=['GET'])
def index():
    return 'Accounts Page'

@accounts_bp.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        user_id = register_form.user_id.data
        user_name = register_form.user_name.data
        user_pw = register_form.user_pw.data
        user_type = register_form.user_type.data

        user = User.get(user_id)
        if user:
            flash('이미 존재하는 사용자입니다.', 'error')
            return render_template('accounts/register.html',
                register_form=register_form)

        user = User(
            user_id,
            User.generate_password_hash(user_pw),
            user_name,
            user_type
        )
        user.save()

        flash('성공적으로 등록되었습니다.', 'success')

        return redirect_back('main.index')
    return render_template('accounts/register.html', register_form=register_form)

@accounts_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user_id = login_form.user_id.data
        user_pw = login_form.user_pw.data

        user = User.get(user_id)
        if not user:
            flash('존재하지 않는 사용자입니다.', 'error')
            return render_template('accounts/login.html', login_form=login_form)

        if not user.check_password(user_pw):
            flash('비밀번호가 틀렸습니다.', 'error')
            return render_template('accounts/login.html', login_form=login_form)

        login_user(user)

        return redirect_back('main.index')
    return render_template('accounts/login.html', login_form=login_form)

@accounts_bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect_back('main.index')