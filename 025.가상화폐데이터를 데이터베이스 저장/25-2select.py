import pandas as pd
import sqlite3
db_path = r''
con = sqlite3.connect(db_path, isolation_level=None)

readed_df = pd.read_sql("SELECT * FROM 'BTC'", con, index_col = 'index')

print(readed_df)