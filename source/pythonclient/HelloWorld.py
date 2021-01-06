import threading
import time

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import  Contract
import pandas

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

def run_loop():
	app.run()


app = IBapi()
app.connect('127.0.0.1', 7497, 0)

# Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1)  # Sleep interval to allow time for connection to server

# Create contract object
eurusd_contract = Contract()
eurusd_contract.symbol = 'JD'
eurusd_contract.secType = 'STK'
eurusd_contract.exchange = 'ISLAND'
eurusd_contract.currency = 'USD'

# Request historical candles
app.reqHistoricalData(1, eurusd_contract, '', '2 D', '1 hour', 'BID', 0, 2, False, [])

time.sleep(5)  # sleep to allow enough time for data to be returned
df = pandas.DataFrame(app.data, columns=['DateTime', 'Close'])
df['DateTime'] = pandas.to_datetime(df['DateTime'], unit='s')
df.to_csv('EURUSD_Hourly.csv')

print(df)




