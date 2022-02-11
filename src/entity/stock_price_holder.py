
"""
    stock_price_holder entity 
    This class is used to store historical pricing information
"""
class StockPriceHolder:
    def __init__(self, stock_name = str, stock_no=str, open=list, close=list, high=list, low=list, volume=list, date=list):
        self.stock_name = stock_name
        self.stock_no = stock_no
        self.open_list = open
        self.close_list = close
        self.high_list = high
        self.low_list = low
        self.volume_list = volume
        self.date_list = date
    
    """
        Below is getter and setter setcion
    """
    def set_stock_name(self, stock_name=str) -> None:
        self.stock_name = stock_name
    def get_stock_name(self) -> str:
        return self.stock_name

    def set_stock_no(self, stock_no=str) -> None:
        self.stock_no = stock_no
    def get_stock_no(self) -> str:
        return self.stock_no

    def set_open_list(self, open=list) -> None:
        self.open_list = open
    def get_open_list(self) -> list:
        return self.open_list
    
    def set_close_list(self, close=list) -> None:
        self.close_list = close
    def get_close_list(self) -> list:
        return self.close_list
    
    def set_high_list(self, high=list) -> None:
        self.high_list = high
    def get_high_list(self) -> list:
        return self.high_list
    
    def set_low_list(self, close=list) -> None:
        self.close_list = close
    def get_low_list(self) -> list:
        return self.close_list
    
    def set_volume_list(self, volume=list) -> None:
        self.volume_list = volume
    def get_volumne_list(self) -> list:
        return self.volume_list
    
    def set_date_list(self, date=list) -> None:
        self.date_list = date
    def get_date_list(self) -> list:
        return self.date_list