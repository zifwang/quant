import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from indicator.moving_average import MovingAverage
from common.moving_average_type import SMA

from entity.stock_price_holder import StockPriceHolder

"""
    simple moving average indictator
"""
class SimpleMovingAverage(MovingAverage):
    def __init__(self, stock_price_holder = StockPriceHolder, window_size = int):
        super().__init__(stock_price_holder, window_size, SMA)
        # set sma
        self.moving_average_list = self.calculate_moving_average(self.get_stock_price_holder().get_close_list(), window_size)

        # set period_list
        self.period_list = self.calculate_period_list(self.get_stock_price_holder().get_date_list(), window_size)
        
    """
        calculate the moving average prices
        @param: close_price_list: close price list
        @param: moving average window size
        @return: sma values
    """
    @staticmethod
    def calculate_moving_average(close_price_list, window_size = int) -> list:
        assert type(close_price_list) == list, "the input must be in list type"
        assert window_size > 1, "window_size must be more than 1"
        assert len(close_price_list) > window_size, "list size must be more than window_size"
        
        moving_average_list = []

        for i in range (0, len(close_price_list)-window_size+1):
            average = np.sum(close_price_list[i:i+window_size]) / window_size
            moving_average_list.append(average)
    
        return moving_average_list
