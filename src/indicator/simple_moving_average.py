import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np
from indicator.moving_average import MovingAverage
from common.moving_average_type import SMA

from entity.stock_price_holder import StockPriceHolder

class SimpleMovingAverage(MovingAverage):
    def __init__(self, stock_price_holder = StockPriceHolder, window_size = int):
        super().__init__(stock_price_holder, window_size, SMA)
        self.calculate_moving_average()
    
    """
        calculate the moving average prices
    """
    def calculate_moving_average(self) -> None:
        window_size = self.get_window_size()                                    # get windows size -- step      # g
        close_price_list = self.get_stock_price_holder().get_close_list()       # get closed price list
        moving_average_list = []

        for i in range (0, len(close_price_list)-window_size+1):
            average = round(np.sum(close_price_list[i:i+window_size]) / window_size, 4)
            moving_average_list.append(average)
        
        # setting
        self.moving_average_list = moving_average_list
        self.period_list = self.get_stock_price_holder().get_date_list()
        self.period_list = self.period_list[window_size-1:]


        
    