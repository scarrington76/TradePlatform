import threading
import time

from ibapi.client import EClient
from ibapi.wrapper import EWrapper, TickTypeEnum
from ibapi.contract import  Contract
import pandas as pd
import stockhash


class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = []

    def error(self, reqId, errorCode, errorString):
        print('Error: ', reqId, " ", errorCode, " ", errorString)

    def contractDetails(self, reqId:int, contractDetails):
        print('contractDetails: ', reqId, ' ', contractDetails)

    def historicalData(self, reqId, bar):
        print(f'Time: {bar.date} Close: {bar.close}')
        self.data.append([bar.date, bar.close])

    def tickPrice(self, reqId, tickType, price, attrib):
        print('Tick Price: Ticker ID:', reqId, 'tickType:', TickTypeEnum.to_str(tickType), 'Price:', price, end=' ')

    def tickSize(self, reqId, tickType, size):
        print('Tick Size. Ticker ID:', reqId, 'ticktype:', TickTypeEnum.to_str(tickType), 'Size:', size)

def run_loop():
    app.run()


app = IBapi()
app.connect('127.0.0.1', 7496, 0)

# Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1)  # Sleep interval to allow time for connection to server
sh = stockhash.Stockhash()

# Create contract object
eurusd_contract = Contract()
eurusd_contract.symbol = 'XOM'
eurusd_contract.secType = 'STK'
eurusd_contract.exchange = 'NYSE'
eurusd_contract.currency = 'USD'


# Request historical candles
result = app.reqMarketDataType(0)
print (type(result))
app.reqMarketDataType(3)
app.reqMktData(1, eurusd_contract, '', False, False, [])

# df = pd.DataFrame(sh.get_stock_details())
# print (df)



# time.sleep(10)  # sleep to allow enough time for data to be returned
# df = pandas.DataFrame(app.data, columns=['DateTime', 'Close'])
# df['DateTime'] = pandas.to_datetime(df['DateTime'], unit='s')
# df.to_csv('EURUSD_Hourly.csv')

# print(df)




