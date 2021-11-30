from . import register
from flask import render_template
from .forms import RegisterFrom


@register.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterFrom()

    return render_template('register.html', form=form)