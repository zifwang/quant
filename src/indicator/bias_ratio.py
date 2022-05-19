import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np

from indicator.simple_moving_average import SimpleMovingAverage
from indicator.weighted_moving_average import WeightedMovingAverage
from entity.stock_price_holder import StockPriceHolder

"""
    Bias Ratio is an indicator used in finance to analyze the return of investment portfolios
    This is a concrete metric that detects valuation bias or deliberate price manipulation of portfolio assets
    In the stock: this shows difference between the moving average of price and the closed price
"""
class BiasRatio:
    def __init__(self, stock_price_holder=StockPriceHolder, window_size=int):
        self.window_size = window_size
        self.period_list = stock_price_holder.get_date_list()
        self.period_list = self.period_list[window_size-1:]
        self.stock_name = stock_price_holder.get_stock_name()
        self.stock_no = stock_price_holder.get_stock_no()
        self.br = self.bias_ratio(stock_price_holder.get_close_list(), window_size)
    
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
    
    def get_period_list(self) -> list:
        return self.period_list
    
    def get_bias_ratio(self) -> list:
        return self.br

    """
        calculate the bias ratio 
        @param: close_price_list: close price list
        @param: window_size: window size
        @return: bais ratio list
    """
    @staticmethod
    def bias_ratio(close_price_list, window_size=int) -> list:
        assert type(close_price_list) == list, "the input must be in list type"
        assert window_size > 1, "window_size must be more than 1"
        assert len(close_price_list) > window_size, "list size must be more than window_size"

        # get simple moving average
        moving_average_list = SimpleMovingAverage.calculate_moving_average(close_price_list, window_size)
        # close price list modify
        close_price_list = close_price_list[window_size-1:]

        # calculate bias ratio
        ma = np.array(moving_average_list)
        cp = np.array(close_price_list)
        br = (cp-ma) / ma

        return br.tolist()