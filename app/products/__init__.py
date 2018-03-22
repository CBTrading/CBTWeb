from pyCBT.providers.oanda import account

client = account.Client()

instruments = account.Instruments(client).table

default_instruments = {"candles": "WTICO_USD", "charts": ["EUR_USD", "USD_JPY", "GBP_USD", "XAU_USD"]}
default_resolutions = {"candles": "H1", "charts": "H1"}
default_datetimes = {"candles": ("2018-02-01", "2018-02-10"), "charts": ("2018-02-01", "2018-02-10")}
default_timezone = "America/New_York"
default_names = {
    "candles": instruments["name"][instruments["symbol"].index(default_instruments["candles"])],
    "charts": [instruments["name"][instruments["symbol"].index(symbol)] for symbol in default_instruments["charts"]]
}
