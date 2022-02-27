import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from entity.stock_price_holder import StockPriceHolder

class MovingAverage:
    def __init__(self, stock_price_holder = StockPriceHolder, window_size = int, ma_type = str):
        assert window_size > 1, "window size has to more than 1"
        self.stock_price_holder = stock_price_holder
        self.ma_type = ma_type
        self.window_size = window_size
        self.moving_average_list = []
        self.period_list = []

    """
        calculate_moving_average
        @param close_price_list: list
        @param window_size: int
    """
    def calculate_moving_average(self, close_price_list, window_size = int) -> list:
        raise NotImplementedError
        
    """
        Below is getter and setter setcion
    """
    def set_stock_price_holder(self, stock_price_holder = StockPriceHolder) -> None:
        self.stock_price_holder = stock_price_holder
    def get_stock_price_holder(self) -> StockPriceHolder:
        return self.stock_price_holder

    def set_ma_type(self, ma_type = str) -> None:
        self.ma_type = ma_type
    def get_ma_type(self) -> str:
        return self.ma_type

    def set_window_size(self, window_size) -> None:
        self.window_size = window_size
    def get_window_size(self) -> int:
        return self.window_size
    
    def get_moving_average_list(self) -> list:
        return self.moving_average_list
    
    def get_period_list(self) -> list:
        return self.period_list
    
    """
        calculate the period list
        @param: period_list: datetime list
        @param: window_size: moving average window size
        @return: modified period_list
    """
    def calculate_period_list(self, period_list, window_size = int) -> list:
        return period_list[window_size-1:]

    """ 
        to_string method to format stock entity into a readable format
        @param: not required
        @return: MovingAverage entity in a readable format string
    """
    def to_string(self):
        periods = str(self.period_list[0]) + "--" + str(self.period_list[len(self.period_list)-1])
        stock_info = self.stock_price_holder.get_stock_name() + "(" + self.stock_price_holder.get_stock_no() + ")"
        ma = str(self.moving_average_list[0]) + "," + str(self.moving_average_list[1]) + "," + str(self.moving_average_list[2]) + "..."

        return '[stock:{stock_info}, moving_average_type:{ma_type}, period:{periods}, calculated_moving_average:{ma}]'.format(stock_info=stock_info, ma_type=self.ma_type, periods=periods, ma=ma)