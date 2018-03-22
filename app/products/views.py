from flask import Blueprint, render_template, url_for, request

from pyCBT.providers.oanda import historical

from . import client, instruments, default_instruments, default_resolutions
from . import default_datetimes, default_timezone, default_names
from .forms import CandlesForm


products = Blueprint("products", __name__, url_prefix="/")

@products.route("/")
def index():
    return render_template("products/index.html.j2")

@products.route("charts/", methods=["GET", "POST"])
def charts():
    form = CandlesForm()
    if form.validate_on_submit():
        default_instruments["candles"] = form.instrument.data
        default_resolutions["candles"] = form.resolution.data
        default_datetimes["candles"] = (form.start_datetime.data.isoformat(), form.end_datetime.data.isoformat())
        default_names["candles"] = instruments["name"][instruments["symbol"].index(form.instrument.data)]

    candles = historical.Candles(
        client=client,
        instrument=default_instruments["candles"],
        resolution=default_resolutions["candles"],
        from_date=default_datetimes["candles"][0],
        to_date=default_datetimes["candles"][1],
        datetime_fmt="JSON",
        timezone=default_timezone
    ).as_dictionary()
    ohlc = []
    volume = []
    for i in xrange(len(candles["Datetime"])):
        ohlc += [[
            candles["Datetime"][i],
            candles["Open"][i],
            candles["High"][i],
            candles["Low"][i],
            candles["Close"][i]
        ]]
        volume += [[
            candles["Datetime"][i],
            candles["Volume"][i]
        ]]

    candles_data = {
        "name": default_names["candles"],
        "ohlc": ohlc,
        "volume": volume
    }

    return render_template(
        "products/charts.html.j2",
        candles=candles_data,
        form=form
    )
