from . import dash
from flask_login import login_required, current_user
from flask import render_template, request, redirect, url_for, flash
from .forms import DashboardForm
from app.models import User


@dash.route('/dashbord', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = DashboardForm()

    # Querystring data on User
    user_info = User.query.filter_by(id=current_user.id).first()
    all_info = User.query.all()

    if request.method == 'POST' and form.validate_on_submit():
        if form.user_data.data:

            flash(user_info)


        elif form.all_data.data:

            flash(all_info)

        else:
            print('nothing')

    return render_template("/dashboard.html", form=form)
