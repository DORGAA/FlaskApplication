from flask_wtf import FlaskForm
from wtforms import SubmitField


class DashboardForm(FlaskForm):
    user_data = SubmitField(label='Account')
    all_data = SubmitField(label='All users')
