import sqlite3
import pandas as pd

conn = sqlite3.connect(r'C:\Users\Ivana\PycharmProjects\TwitterSentimentAnalysis\stock.db')
df = pd.read_sql_query("SELECT * FROM gme_stock_data", conn)
print(df)
