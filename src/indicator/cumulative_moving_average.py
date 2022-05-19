import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np

from indicator.moving_average import MovingAverage
from common.moving_average_type import CMA
from entity.stock_price_holder import StockPriceHolder

"""
    Cumulative Moving Average extends the Moving Average(MovingAverage)
    CMA is also frequently called a running average or a long running average although the term running average is also used as synonym for a moving average.
    The data arrives in an orderly data stream and the statistician would like to calculate the average of all data up until the current data point, which in itself moves with time
"""
class CumulativeMovingAverage(MovingAverage):
    def __init__(self, stock_price_holder=StockPriceHolder, window_size=int):
        super().__init__(stock_price_holder, window_size, CMA)
    
        # set cma
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
        
        pointer = 0
        moving_average_list = []

        for i in range(window_size-1, len(close_price_list)):
            if i == window_size-1:
                cma = np.sum(close_price_list[0:i+1]) / window_size
                moving_average_list.append(cma)
            else:
                # CMAn+1 = CMAn + (Xn+1 - CMAn)/(n+1) -- n is current position
                cma = (close_price_list[i] + i * moving_average_list[pointer])/(i+1)
                moving_average_list.append(cma)
                pointer += 1
        
        return moving_average_list
    
    """
        calculate the period list
        @param: period_list: datetime list
        @param: window_size: moving average window size
        @return: modified period_list
    """
    def calculate_period_list(self, period_list, window_size = int) -> list:
        return period_list[window_size-1:]
