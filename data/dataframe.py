import pandas as pd
import sqlite3

#  twitt_cursor.execute('DELETE FROM tweet_sentiment_analysis;')
#  twitt_cursor.execute('DROP TABLE IF EXISTS tweet_sentiment_analysis;')
#  twitt_connection.commit()
#  stock_cursor.execute('DELETE FROM gme_stock_data;')
#  stock_cursor.execute('DROP TABLE IF EXISTS gme_stock_data;')
#  stock_connection.commit()


class DataForPlotting:

    def __init__(self):
        self.twitt_connection = sqlite3.connect(r'C:\Users\Ivan\PycharmProjects\SCRAPING-StockTwitter\twitter.db')
        self.twitt_cursor = self.twitt_connection.cursor()
        self.stock_connection = sqlite3.connect(r'C:\Users\Ivan\PycharmProjects\SCRAPING-StockTwitter\stock.db')
        self.stock_cursor = self.stock_connection.cursor()

    def get_df(self):
        df_twitt = pd.read_sql_query(
            'SELECT tweet_datetime, subjectivity, polarity FROM tweet_sentiment_analysis', self.twitt_connection)
        df_twitt['tweet_datetime'] = pd.to_datetime(df_twitt['tweet_datetime']).dt.date
        df_twitt['subjectivity'] = pd.to_numeric(df_twitt['subjectivity'])
        df_twitt['polarity'] = pd.to_numeric(df_twitt['polarity'])
        df_twitt = df_twitt.rename(columns={'tweet_datetime': 'date_time'})
        df_twitt = df_twitt.groupby('date_time').mean()

        df_stock = pd.read_sql_query('SELECT * FROM gme_stock_data', self.stock_connection)
        df_stock['date_time'] = pd.to_datetime(df_stock['date_time']).dt.date
        df_stock = df_stock.groupby('date_time').mean()

        df_merged = pd.merge(df_stock, df_twitt, on=["date_time"])
        df_merged = df_merged.fillna(0)
        df_merged['datetime'] = df_merged.index
        df_merged.reset_index(drop=True, inplace=True)
        df_merged['month'] = pd.DatetimeIndex(df_merged['datetime']).month
        df_merged['days'] = df_merged.index + 1

        return df_merged
