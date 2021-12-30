import sqlite3
import pandas as pd
import logging
import time

try:
    connection = sqlite3.connect(r'C:\Users\Ivana\PycharmProjects\TwitterSentimentAnalysis\stock.db')
    start_time = time.time()
    logging.basicConfig(filename='logs.txt',
                        filemode='a',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S')
    logging.info(f'Pocetak izvrsavanja zadatka.')

    df = pd.read_sql_query("SELECT * FROM gme_stock_data", connection)
    print(df)

except Exception:
    logging.exception(f'Dogodila se greska sljedeceg sadrzaja:')
    #stock.rollback_connection()
else:
    logging.info('Uspjesno izvrsen zadatak.')
finally:
    #stock.closing_connection()
    logging.info(f'Obrada trajala: {time.strftime("%H sati, %M minuta i %S sekundi.", time.gmtime(time.time() - start_time))}\n')
