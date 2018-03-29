from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, StringField
from wtforms.validators import required
from wtforms.widgets import HTMLString, html_params

from . import instruments


class CandlesForm(FlaskForm):
    instrument = SelectField("Instrument", choices=zip(instruments["symbol"], instruments["name"]))
    resolution = SelectField("Resolution", choices=zip("M15 M30 H1 H6 H12 D".split(), "M15 M30 H1 H6 H12 D".split()))
    start_datetime = DateField("Start at", validators=[required()])
    end_datetime = DateField("End at", validators=[required()])
