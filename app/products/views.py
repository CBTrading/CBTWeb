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
    if request.method == "POST":
        pass
    #   get historical parameters from POST request
    #   update charts with input parameters
    #   update defaults to input parameters
    else:
        pass
    #   show charts for default historical values (now)
        candles = historical.Candles(
            client=client,
            instrument=default_instruments["candles"],
            resolution=default_resolutions["candles"],
            from_date=default_datetimes["candles"][0],
            to_date=default_datetimes["candles"][1],
            datetime_fmt="JSON",
            timezone=default_timezone
        )
        candles = candles.as_dictionary()
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

    #   show the form for updating historical parameters

    return render_template(
        "products/charts.html.j2",
        candles_symbol=instruments.table["name"][instruments.table["symbol"].index(default_instruments["candles"])],
        ohlc=ohlc,
        volume=volume
    )
