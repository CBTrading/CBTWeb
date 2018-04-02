from pyCBT.providers.oanda import account


client = account.Client()
instruments = account.Instruments(client).table
charts_time_groups = {
    "H1": [8, 12],
    "D": [5, 10, 14, 22]
}
settings_default = {
    "candles_symbol": "WTICO_USD",
    "charts_symbols": ["EUR_USD", "USD_JPY", "GBP_USD", "XAU_USD"],
    "resolution": "H1",
    "datetimes": ("2017-01-01", "2018-01-01"),
    "timezone": "America/New_York",
    "timeframe": charts_time_groups["H1"][0],
    "price": "Close"
}
