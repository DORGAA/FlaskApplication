from . import dash
from flask_login import login_required, current_user
from flask import render_template, request
from .forms import DashboardForm
from app.models import User


@dash.route('/dashbord', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = DashboardForm()
    if request.method == 'GET':
        user_info = User.query.filter_by(id=current_user.id).first()

    return render_template("/dashboard.html", user_info=user_info)
