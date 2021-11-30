from . import login
from flask import render_template
from .forms import LoginForm


@login.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    return render_template("/login.html", form=form)
