class Stockhash():
    '''Holds the contract info for the stocks I am actively tracking with this tool'''
    def __init__(self):
        self.stock_details = {'Stocks': {'EPD': {'exchange': 'NYSE', 'secType': 'STK', 'currency': 'USD'},
                                    'HD': {'exchange': 'NYSE'},
                                    'RGA': {'exchange': 'NYSE'},
                                    'FHN': {'exchange': 'NYSE'},
                                    'EVR': {'exchange': 'NYSE'},
                                    'LOMA': {'exchange': 'NYSE'},
                                    'MDC': {'exchange': 'NYSE'}
                                    }}

    def get_stock_details(self):
        return self.stock_details
