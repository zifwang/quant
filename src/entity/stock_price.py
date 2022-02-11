from datetime import datetime

"""
    Stock_price Entity 
    This entity uses to hold information of each stock
"""
class StockPrice:
    def __init__(self, stock_name, stock_no, open=None, close=None, high=None, low=None, volume=None, date=None):
        self.stock_name = stock_name
        self.stock_no = stock_no
        self.open_price = open
        self.close_price = close
        self.high_price = high
        self.low_price = low
        self.volume = volume
        self.dateTime = date

    """
        Below is getter and setter setcion
    """
    def set_stock_name(self, stock_name: str) -> None:
        self.stock_name = stock_name
    def get_stock_name(self) -> str:
        return self.stock_name
    
    def set_stock_no(self, stock_no: str) -> None:
        self.stock_no = stock_no
    def get_stock_no(self) -> str:
        return self.stock_no

    def set_high_price(self, price: float) -> None:
        self.high_price = price
    def get_high_price(self) -> float:
        return self.high_price
    
    def set_low_price(self, price: float) -> None:
        self.low_price = price
    def get_low_price(self) -> float:
        return self.low_price

    def set_open_price(self, price: float) -> None:
        self.open_price = price
    def get_open_price(self) -> float:
        return self.open_price
    
    def set_close_price(self, price: float) -> None:
        self.close_price = price
    def get_close_price(self) -> float:
        return self.close_price

    def set_volume(self, volume: int) -> None:
        self.volume = volume
    def get_volume(self) -> int:
        return self.volume

    def set_datetime(self, date: datetime) -> None:
        self.dateTime = date
    def get_datetime(self) -> datetime:
        return self.dateTime

    """
        to_string method to format stock entity into a readable format
        @param: not required
        @return: stock entity in a readable format string
    """
    def to_string(self) -> str:
        return '[stock_name:{name}, stock_no:{no}, date:{date}, open:{open}, close:{close}, high:{high}, low:{low}, volume{vol}]'.format(name=self.stock_name, no=self.stock_no, date=self.dateTime, open=self.open_price, close=self.close_price, high=self.high_price, low=self.low_price, vol=self.volume) 
