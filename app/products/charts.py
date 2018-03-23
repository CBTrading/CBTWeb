from pyCBT.providers.oanda import historical


# TODO: function to build candles data ready for Highcharts
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
# TODO: function to build volatility data ready for Highcharts
