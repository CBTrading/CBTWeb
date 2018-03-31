from flask import Blueprint, render_template, url_for, request

from . import client, instruments, settings_default
from .forms import CandlesForm
from .charts import Datasets


products = Blueprint("products", __name__, url_prefix="/")

@products.route("/")
def index():
    return render_template("products/index.html.j2")

@products.route("charts/", methods=["GET", "POST"])
def charts():
    datasets = Datasets(client, settings=settings_default)
    form = CandlesForm()
    if form.validate_on_submit():
        datasets.settings.update({
            "candles_symbol": form.instrument.data,
            "resolution": form.resolution.data,
            "datetimes": form.datetime_range.data
        })
    datasets.download()

    return render_template(
        "products/charts.html.j2",
        form=form,
        candles=datasets.get_highcharts_candles(),
        correlations=datasets.get_highcharts_correlations(),
        heatmap=datasets.get_highcharts_heatmap(),
        volatility=datasets.get_highcharts_volatility()
    )
