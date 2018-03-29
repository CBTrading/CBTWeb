from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, StringField
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
        '<div class="input-group input-daterange col-md-12">'
        '<input %(input-1)s>'
        '<div class="input-group-addon">to</div>'
        '<input %(input-2)s>'
        '</div>'
    )

    def __call__(self, field, **kwargs):
        if not field.data:
            data_1, data_2 = "", ""
        else:
            data_1, data_2 = field.data

        return HTMLString(self.data_template % {
            "input-1": html_params(id="{}-1".format(field.id), name="{}".format(field.name), type="text", value=data_1, **kwargs),
            "input-2": html_params(id="{}-2".format(field.id), name="{}".format(field.name), type="text", value=data_2, **kwargs)
        })

class CandlesForm(FlaskForm):
    instrument = SelectField("Instrument", choices=zip(instruments["symbol"], instruments["name"]))
    resolution = SelectField("Resolution", choices=zip("M15 M30 H1 H6 H12 D".split(), "M15 M30 H1 H6 H12 D".split()))
    datetime_range = DateRangeField("Date range", validators=[required()], widget=DateRangePickerWidget())
