class Stockhash():
    '''Holds the contract info for the stocks I am actively tracking with this tool'''
    def __init__(self):
        self.stock_details = {'Stocks': {'EPD': {'Exchange': 'NYSE'},
                                    'HD': {'Exchange': 'NYSE'},
                                    'RGA': {'Exchange': 'NYSE'},
                                    'FHN': {'Exchange': 'NYSE'},
                                    'EVR': {'Exchange': 'NYSE'},
                                    'LOMA': {'Exchange': 'NYSE'},
                                    'MDC': {'Exchange': 'NYSE'}
                                    }}

    def get_stock_details(self):
        return self.stock_details
