from pyCBT.providers.oanda import account

client = account.Client()

instruments = account.Instruments(client).table

candles_def = {
    "symbol": "WTICO_USD",
    "name": instruments["name"][instruments["symbol"].index("WTICO_USD")],
    "resolution": "H1",
    "datetimes": ("2018-02-01", "2018-02-10"),
    "timezone": "America/New_York"
}
