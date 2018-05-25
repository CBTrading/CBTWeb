from pyCBT.providers.oanda import account
import numpy as np

client = account.Client()

markets = {"forex": "Forex", "cfds": "CFDs", "precious-metals": "Metals"}
instrument_names = [
    "DAX",
    "Nikkei",
    "DJI",
    "S&P 500",
    "NASDAQ",
    "FTSE",
    "WTI Crude Oil",
    "Brent Crude Oil",
    "BTC/USD",
    "Dollar Index",
    "EUR/USD",
    "GBP/USD",
    "USD/CHF",
    "USD/JPY",
    "EUR/CHF",
    "EUR/GBP",
    "EUR/JPY",
    "GBP/CHF",
    "GBP/JPY",
    "AUD/USD",
    "NZD/USD",
    "USD/CAD",
    "EUR/AUD",
    "EUR/CAD",
    "GBP/AUD",
    "GBP/CAD",
    "AUD/CHF",
    "AUD/JPY",
    "CHF/JPY",
    "CAD/CHF",
    "CAD/JPY",
    "NZD/CHF",
    "NZD/JPY",
    "AUD/CAD",
    "AUD/NZD",
    "NZD/CAD",
    "EUR/NZD",
    "GBP/NZD",
    "EUR/NOK",
    "EUR/ZAR",
    "USD/MXN",
    "USD/NOK",
    "USD/RUB",
    "USD/SEK",
    "USD/SGD",
    "USD/ZAR",
    "EUR/TRY",
    "USD/TRY",
    "XAU/USD",
    "XAG/USD"
]
oanda_symbols = [
    "DE30_EUR",
    "JP225_USD",
    "US30_USD",
    "SPX500_USD",
    "NAS100_USD",
    "UK100_EUR",
    "WTICO_USD",
    "BCO_USD",
    "BTC_USD",
    None,
    "EUR_USD",
    "GBP_USD",
    "USD_CHF",
    "USD_JPY",
    "EUR_CHF",
    "EUR_GBP",
    "EUR_JPY",
    "GBP_CHF",
    "GBP_JPY",
    "AUD_USD",
    "NZD_USD",
    "USD_CAD",
    "EUR_AUD",
    "EUR_CAD",
    "GBP_AUD",
    "GBP_CAD",
    "AUD_CHF",
    "AUD_JPY",
    "CHF_JPY",
    "CAD_CHF",
    "CAD_JPY",
    "NZD_CHF",
    "NZD_JPY",
    "AUD_CAD",
    "AUD_NZD",
    "NZD_CAD",
    "EUR_NZD",
    "GBP_NZD",
    "EUR_NOK",
    "EUR_ZAR",
    "USD_MXN",
    "USD_NOK",
    "USD_RUB",
    "USD_SEK",
    "USD_SGD",
    "USD_ZAR",
    "EUR_TRY",
    "USD_TRY",
    "XAU_USD",
    "XAG_USD"
]
fxchoice_symbols = []
market_names = []
for market in sorted(markets):
    symbols = np.genfromtxt("./app/static/data/{}.csv".format(market), usecols=(0,), delimiter=",", skip_header=1, dtype=np.str)
    fxchoice_symbols += list(symbols)
    market_names += [markets.get(market)] * symbols.size

instruments = {symbol: {"FXChoice": fxchoice_symbols[i], "name": instrument_names[i], "type": market_names[i]} for i, symbol in enumerate(oanda_symbols)}

charts_time_groups = {
    "H1": [4, 12],
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
