from pyCBT.providers.oanda import account

client = account.Client()

instruments = account.Instruments(client).table

resolution_def = "H1"
datetimes_def = ("2018-02-01", "2018-02-10")
timezone_def = "America/New_York"

candles_symbol = "WTICO_USD"
charts_symbols = ["EUR_USD", "USD_JPY", "GBP_USD", "XAU_USD"]
charts_time_groups = {"H1": [4, 6, 8, 12], "D": [5, 10, 14, 22]}

candles_def = {
    "symbol": candles_symbol,
    "name": instruments["name"][instruments["symbol"].index(candles_symbol)],
    "resolution": resolution_def,
    "datetimes": datetimes_def,
    "timezone": timezone_def
}
}
