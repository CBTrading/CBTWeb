from flask import Blueprint, render_template, url_for, request

from . import client, instruments, candles_def, correlations_def
from .forms import CandlesForm
from .charts import get_candles_data, get_correlation_data


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
            "datetimes": form.datetime_range.data
        })
        correlations_def.update({
            "refer_symbol": form.instrument.data,
            "name": instruments["name"][instruments["symbol"].index(form.instrument.data)],
            "resolution": form.resolution.data,
            "datetimes": form.datetime_range.data
        })

    candles_data = get_candles_data(client, **candles_def)
    correlations_data = get_correlation_data(client, **correlations_def)

    return render_template(
        "products/charts.html.j2",
        candles=candles_data,
        correlations=correlations_data,
        form=form
    )
