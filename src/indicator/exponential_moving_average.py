import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import numpy as np

from indicator.moving_average import MovingAverage
from common.moving_average_type import EMA
from entity.stock_price_holder import StockPriceHolder

class ExponentialMovingAverage(MovingAverage):
    def __init__(self, stock_price_holder=StockPriceHolder, window_size=int, alpha=None, adjust=False):
        super().__init__(stock_price_holder, window_size, EMA)

        # set smoothing factor
        if alpha:
            assert 0 < alpha <= 1.0, "smoothing factor(alpha) is not in the range"
            self.alpha = alpha
        else:
            assert window_size > 0, "window_size must be more than 0"
            self.alpha = 2/(1+window_size)  # default alpha

        # set ema
        self.moving_average_list = self.calculate_moving_average(self.get_stock_price_holder().get_close_list(), window_size, self.alpha, adjust)

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
        calculate the exponential moving average prices
        @param: close_price_list: close price list
        @param: moving average window size
        @return: ema values
    """
    @staticmethod
    def calculate_moving_average(close_price_list, window_size=int, alpha=None, adjust=False) -> list:
        assert type(close_price_list) == list, "the input must be in list type"
        assert window_size > 1, "window_size must be more than 1"
        assert len(close_price_list) > window_size, "list size must be more than window_size"
        
        # set smoothing factor
        if alpha:
            assert 0 < alpha <= 1.0, "smoothing factor(alpha) is not in the range"
        else:
            alpha = 2/(1+window_size)   # default alpha

        close_price_list = np.array(close_price_list)
        lenght = close_price_list.shape[0]
        moving_average_list = []        # init. moving average list

        if adjust:
            weights = [pow(1-alpha, t) for t in range(len(close_price_list))]       # init. weights for ema calculated by adjusted method
            weights = np.array(weights[::-1])
            
            for i in range(0, lenght):
                # ma = (weights[0]*close[i] + weights[1]*close[i-1] + ... + weights[t]*close[0])/sum(weights)
                ma = np.dot(close_price_list[:i+1],weights[lenght-i-1:lenght])/np.sum(weights[lenght-i-1:lenght])
                moving_average_list.append(ma.item())

        else:
            moving_average_list.append(close_price_list[0])         
            for i in range(1, lenght):
                # alpha*(closePrice_today - ema_yesterday) + ema_yesterday
                ema_today = close_price_list[i] * alpha + moving_average_list[i-1] * (1 - alpha) 
                moving_average_list.append(ema_today.item())
        
        return moving_average_list

    """
        calculate the period list
        @param: period_list: datetime list
        @param: window_size: moving average window size
        @return: modified period_list
    """
    def calculate_period_list(self, period_list, window_size = None) -> list:
        return period_list
    
if __name__ == "__main__":
    close = [1,2,3,4,5,6,7,8,9]
    ema = ExponentialMovingAverage.calculate_moving_average(close, -1)