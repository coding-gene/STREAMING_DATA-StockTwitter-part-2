# https://github.com/anubhavanand12qw/STOCK-PRICE-PREDICTION-USING-TWITTER-SENTIMENT-ANALYSIS/blob/master/STOCK%20PREDICTION%20USING%20TWITTER%20SENTIMENT%20ANALYSIS%20PROJECT%20(FINAL)%20-%20Updated.ipynb
# https://github.com/talaikis/StockTalk3
import sqlite3
import pandas as pd
import logging
import time

pd.set_option('display.max_rows', 40)
pd.set_option('display.max_columns', 40)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', 300)

start_time = time.time()
logging.basicConfig(filename='logs.txt',
                    filemode='a',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.info(f'Job started.')
# noinspection PyBroadException
try:
    connection = sqlite3.connect(r'C:\Users\Ivan\PycharmProjects\SCRAPING-StockTwitter\twitter.db')
    cursor = connection.cursor()
    #  cursor.execute('DELETE FROM gme_stock_data;')
    #  cursor.execute('DROP TABLE IF EXISTS tweet_sentiment_analysis;')
    #  connection.commit()

    df = pd.read_sql_query('SELECT * FROM tweet_sentiment_analysis', connection)
    print(df)
    print(df)

except Exception:
    logging.exception(f'An error occurred during job performing:')
    # stock.rollback_connection()
else:
    logging.info('Job ended.')
finally:
    # stock.closing_connection()
    logging.info(
        f'Job duration: {time.strftime("%H hours, %M minutes, %S seconds.", time.gmtime(time.time() - start_time))}\n')
