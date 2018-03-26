import numpy as np
from pyCBT.providers.oanda import historical


# TODO: function to build other_candles data ready for Highcharts
def get_candles_data(client, **kwargs):
    """Returns the candles data dictionary
    """
    candles = historical.Candles(
        client=client,
        instrument=kwargs.get("symbol"),
        resolution=kwargs.get("resolution"),
        from_date=kwargs.get("datetimes")[0],
        to_date=kwargs.get("datetimes")[1],
        datetime_fmt="JSON",
        timezone=kwargs.get("timezone")
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

    data = {
        "name": kwargs.get("name"),
        "ohlc": ohlc,
        "volume": volume
    }

    return data

# TODO: function to build correlation data ready for Highcharts
def get_correlation_data(client, **kwargs):
    # download reference candles
    price_i = historical.Candles(
        client=client,
        instrument=kwargs.get("refer_symbol"),
        resolution=kwargs.get("resolution"),
        from_date=kwargs.get("datetimes")[0],
        to_date=kwargs.get("datetimes")[1],
        datetime_fmt="JSON",
        timezone=kwargs.get("timezone")
    ).as_dictionary()[kwargs.get("price", "Close")][-kwargs.get("timeframe"):]
    # download datasets
    data = {
        "name": kwargs.get("name"),
        "categories": kwargs.get("categories"),
        "series": {
            "negative": [],
            "positive": []
        }
    }
    for symbol in kwargs.get("other_symbols"):
        price_j = historical.Candles(
            client=client,
            instrument=symbol,
            resolution=kwargs.get("resolution"),
            from_date=kwargs.get("datetimes")[0],
            to_date=kwargs.get("datetimes")[1],
            datetime_fmt="JSON",
            timezone=kwargs.get("timezone")
        ).as_dictionary()[kwargs.get("price", "Close")][-kwargs.get("timeframe"):]
        # compute correlations
        corr_ij = np.corrcoef(price_i, price_j)[1, 0]
        # format datasets in lists ordered according to names list
        if corr_ij < 0:
            data["series"]["negative"] += [-corr_ij]
            data["series"]["positive"] += [0.0]
        else:
            data["series"]["negative"] += [0.0]
            data["series"]["positive"] += [corr_ij]

    return data

# TODO: function to build volatility data ready for Highcharts
