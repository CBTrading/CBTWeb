from flask import Blueprint, render_template, url_for, request

from . import client, instruments, candles_def
from .forms import CandlesForm
from .charts import get_candles_data


products = Blueprint("products", __name__, url_prefix="/")

@products.route("/")
def index():
    return render_template("products/index.html.j2")

@products.route("charts/", methods=["GET", "POST"])
def charts():
    form = CandlesForm()
    if form.validate_on_submit():
        candles_def.update({
            "symbol": form.instrument.data,
            "name": instruments["name"][instruments["symbol"].index(form.instrument.data)],
            "resolution": form.resolution.data,
            "datetimes": (form.start_datetime.data.isoformat(), form.end_datetime.data.isoformat())
        })

    candles_data = get_candles_data(client, **candles_def)

    return render_template("products/charts.html.j2", candles=candles_data, form=form)
