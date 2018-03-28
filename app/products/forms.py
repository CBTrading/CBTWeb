from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, StringField
from wtforms.validators import required
from wtforms.widgets import HTMLString, html_params

from . import instruments

class DatePickerWidget(object):
    """
    Date Time picker from Eonasdan GitHub

    https://github.com/dpgaspar/Flask-AppBuilder/blob/master/flask_appbuilder/fieldwidgets.py#L5
    """
    data_template = ('<div id="datetimepicker" class="input-append">'
                     '<input data-format="yyyy-MM-dd" type="text"></input>'
                     '<span class="add-on">'
                     '<i data-time-icon="icon-time" data-date-icon="icon-calendar"></i>'
                     '</span>'
                     '</div>')
                    # '<div class="input-group date appbuilder_date" id="datepicker">'
                    # '<span class="input-group-addon"><i class="fa fa-calendar cursor-hand"></i>'
                    # '</span>'
                    # '<input data-format="yyyy-MM-dd" %(text)s/>'
                    # '</div>'

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('name', field.name)
        if not field.data:
            field.data = ""
        template = self.data_template

        return HTMLString(template % {'text': html_params(type='text',
                                      value=field.data,
                                      **kwargs)
                                      })

class CandlesForm(FlaskForm):
    instrument = SelectField("Instrument", choices=zip(instruments["symbol"], instruments["name"]))
    resolution = SelectField("Resolution", choices=zip("M15 M30 H1 H6 H12 D".split(), "M15 M30 H1 H6 H12 D".split()))
    start_datetime = DateField(
        "Start at",
        [required()],
        widget=DatePickerWidget()
    )
    end_datetime = DateField(
        "End at",
        [required()],
        widget=DatePickerWidget()
    )
