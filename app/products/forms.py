from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, StringField, SelectMultipleField
from wtforms.validators import required
from wtforms.widgets import HTMLString, html_params

from . import instruments


class DateRangeField(DateField):

    def _value(self):
        print self.data
        if self.data:
            return u" ".join(self.data)
        else:
            return u""

    def process_formdata(self, date_range):
        if date_range:
            self.data = date_range
        else:
            self.data = []

class DateRangePickerWidget(object):
    data_template = (
        '<div id="datepicker" class="input-daterange input-group">'
        '<input %(input-1)s name="start">'
        '<div class="input-group-addon">to</div>'
        '<input %(input-2)s name="end">'
        '</div>'
    )

    def __call__(self, field, **kwargs):
        kwargs.setdefault("type", "text")
        kwargs.setdefault("id", field.id)
        kwargs.setdefault("name", field.name)
        if not field.data:
            data_1, data_2 = "", ""
        else:
            data_1, data_2 = field.data

        return HTMLString(self.data_template % {
            "input-1": html_params(value=data_1, **kwargs),
            "input-2": html_params(value=data_2, **kwargs)
        })

class CandlesForm(FlaskForm):
    instrument = SelectField("Instrument", choices=[(symbol, instruments[symbol]["name"]) for symbol in instruments.keys()])
    resolution = SelectField("Resolution", choices=zip("M15 M30 H1 H6 H12 D".split(), "M15 M30 H1 H6 H12 D".split()))
    datetime_range = DateRangeField("Date range", validators=[required()], widget=DateRangePickerWidget())

class ChartsForm(FlaskForm):
    instrument_types = SelectMultipleField("Instrument type", choices=zip(("com", "met", "exo", "cdf"), ("common", "metals", "exotic", "CDFs")))
    instrument = SelectField("Reference instrument", choices=[(symbol, instruments[symbol]["name"]) for symbol in instruments.keys()])
    vs_instruments = SelectMultipleField("Instruments", choices=[(symbol, instruments[symbol]["name"]) for symbol in instruments.keys()])
