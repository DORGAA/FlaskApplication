from . import login, logout
from flask import render_template, request, redirect, url_for
from flask_login import login_required
from .forms import LoginForm
from app.models import User
from flask_bcrypt import check_password_hash
from flask_login.utils import login_user, logout_user


@login.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user = User.query.filter_by(email=form.email.data).first()
        if new_user and check_password_hash(new_user.password, form.password.data):

            login_user(new_user)
            return redirect(url_for('dashboard.dashboard'))
        else:
            return redirect(url_for('login_out.login_out'))
    return render_template("/login.html", form=form)


@logout.route('/logout')
@login_required
def logout():
    logout_user()

    return redirect(url_for('login_out.login'))
