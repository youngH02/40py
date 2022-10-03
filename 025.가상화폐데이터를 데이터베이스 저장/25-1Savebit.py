#pip install pyupbit

import pyupbit

# #가상화폐 리스트
# coin_lists = pyupbit.get_tickers(fiat='KRW')
# print(coin_lists)

# #가상화폐 시세
# price_now = pyupbit.get_current_price(["KRW-BTC","KRW-ETH"])
# print(price_now)

ticker = 'KRW-BTC'
interval = 'minute1'
to='2022-10-03 14:00'
count = 200
price_now = pyupbit.get_ohlcv(ticker = ticker, interval = interval, to=to, count=count)

db_path = ''

con = sqlite3.connect(db_path, isolation_level=None)
price_now.to_sql('BTC',con, if_exists = 'append')

con.close