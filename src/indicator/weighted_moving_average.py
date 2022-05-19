import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
import pandas as pd

from indicator.moving_average import MovingAverage
from common.moving_average_type import WMA
from entity.stock_price_holder import StockPriceHolder

"""
    Weighted Moving Average
    A Weighted Moving Average puts more weight on recent data and less on past data.
"""
class WeightedMovingAverage(MovingAverage):
    def __init__(self, stock_price_holder=StockPriceHolder, window_size=int):
        super().__init__(stock_price_holder, window_size, WMA)

        # set wma
        self.moving_average_list = self.calculate_moving_average(self.get_stock_price_holder().get_close_list(), window_size)

        # set period_list
        self.period_list = self.calculate_period_list(self.get_stock_price_holder().get_date_list(), window_size)

    """
        calculate the cumulative moving average prices
        @param: close_price_list: close price list
        @param: moving average window size
        @return: cma values
    """
    @staticmethod
    def calculate_moving_average(close_price_list, window_size=int) -> list:
        assert type(close_price_list) == list, "the input must be in list type"
        assert window_size > 1, "window_size must be more than 1"
        assert len(close_price_list) > window_size, "list size must be more than window_size"
        
        moving_average_list = []

        weights = np.arange(1, window_size + 1)
        df = pd.DataFrame({'val': close_price_list})
        moving_average_list = df['val'].rolling(window_size).apply(lambda x: np.dot(x, weights) /
                                       weights.sum()).to_list()

        return moving_average_list[window_size-1:]
    
    """
        calculate the period list
        @param: period_list: datetime list
        @param: window_size: moving average window size
        @return: modified period_list
    """
    def calculate_period_list(self, period_list, window_size = int) -> list:
        return period_list[window_size-1:]