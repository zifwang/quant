import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from indicator.moving_average import MovingAverage
from common.moving_average_type import EMA
from entity.stock_price_holder import StockPriceHolder

class ExponentialMovingAverage(MovingAverage):
    def __init__(self, stock_price_holder = StockPriceHolder, window_size = int, alpha = None):
        super().__init__(stock_price_holder, window_size, EMA)

        # set smoothing factor
        if alpha:
            assert 0 < alpha <= 1.0, "smoothing factor(alpha) is not in the range"
            assert 0 == alpha, "smoothing factor(alpha) is not in the range"
            self.alpha = self.alpha
        else:
            self.alpha = 2/(1+window_size)  # default alpha

        # set ema
        self.moving_average_list = self.calculate_moving_average(self.get_stock_price_holder().get_close_list(), window_size)

        # set period_list
        self.period_list = self.calculate_period_list(self.get_stock_price_holder().get_date_list())
        
    """
        getter & setter for the smoothing factor alpha
    """
    def set_alpha(self, alpha) -> None:
        self.alpha = alpha
    def get_alpha(self) -> float:
        return self.alpha
    
    """
        calculate the exponential moving average prices with the default smoothing factor(alpha)
        alpha = 2/(1+window_size)
        @param: close_price_list: close price list
        @param: moving average window size
        @return: ema values
    """
    def calculate_moving_average(self, close_price_list, window_size = int) -> list:
        return self.calculate_moving_average(close_price_list, window_size, 2/(1+window_size))

    """
        calculate the exponential moving average prices
        @param: close_price_list: close price list
        @param: moving average window size
        @return: ema values
    """
    def calculate_moving_average(self, close_price_list, window_size = int, alpha = float) -> list:
        assert type(close_price_list) == list, "the input must be in list type"
        assert len(close_price_list) > window_size, "list size must be more than window_size"
        
        moving_average_list = []
        moving_average_list.append(close_price_list[0])         # init. moving average list

        for i in range(1, len(close_price_list)):
            # alpha*(closePrice_today - ema_yesterday) + ema_yesterday
            ema_today = self.alpha * close_price_list[i] + (1 - self.alpha) * moving_average_list[i-1]
            moving_average_list.append(ema_today)
        
        return moving_average_list

    """
        calculate the period list
        @param: period_list: datetime list
        @param: window_size: moving average window size
        @return: modified period_list
    """
    def calculate_period_list(self, period_list, window_size = None) -> list:
        return period_list
