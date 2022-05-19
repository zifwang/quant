import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
import numpy as np

from entity.stock_price_holder import StockPriceHolder
from indicator.simple_moving_average import SimpleMovingAverage
from indicator.exponential_moving_average import ExponentialMovingAverage

class RelativeStrengthIndex:
    def __init__(self, stock_price_holder = StockPriceHolder, window_size = 14, rs_type = "SMMA"):
        self.window_size = window_size
        self.period_list = self.calculate_period_list(stock_price_holder.get_date_list(), window_size, rs_type)
        self.stock_name = stock_price_holder.get_stock_name()
        self.stock_no = stock_price_holder.get_stock_no()
        self.rs_type = rs_type
        self.rsi_list = self.rsi(stock_price_holder.get_close_list(), window_size, rs_type)
    
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
    
    def get_rs_type(self) -> str:
        return self.rs_type

    def get_period_list(self) -> list:
        return self.period_list

    def get_rsi_list(self) -> list:
        return self.rsi_list

    """
        calculate the relative strength index
        @param: close_price_list: close price list
        @param: window_size: window size is default to 14
        @param: rs_type: the relative strength is often defined by following method:
            1. simple moving average (SMA), 
            2. exponential moving average (EMA), 
            3. n-period smoothed or modified moving average (SMMA), an EMA with a = 1/period
            rs_type is default to SMMA
        @return: rsi list
    """
    @staticmethod
    def rsi(close_price_list=[], window_size = 14, rs_type = "SMMA"):
        assert rs_type == "SMMA" or rs_type == "EMA" or rs_type == "SMA", "RSI calculation only support SMMA, EMA, and SMA"
        assert window_size > 1, "window_size must be more than 1"
        assert len(close_price_list) > window_size, "list size must be more than window_size"

        # get the positive gain array and negative gain array
        pos_change, neg_change = [], []

        prev = close_price_list[0]
        for i in range (1, len(close_price_list)):
            diff = close_price_list[i] - prev
            if diff >= 0:
                pos_change.append(diff)
                neg_change.append(0)
            else:
                pos_change.append(0)
                neg_change.append(abs(diff))
            prev = close_price_list[i]
            
        if rs_type == "SMMA":
            alpha = 1/(window_size)
            gain_average = ExponentialMovingAverage.calculate_moving_average(pos_change, window_size, alpha)
            loss_average = ExponentialMovingAverage.calculate_moving_average(neg_change, window_size, alpha)
        if rs_type == "EMA":
            alpha = 2/(1+window_size)
            gain_average = ExponentialMovingAverage.calculate_moving_average(pos_change, window_size, alpha)
            loss_average = ExponentialMovingAverage.calculate_moving_average(neg_change, window_size, alpha)
        if rs_type == "SMA":
            gain_average = SimpleMovingAverage.calculate_moving_average(pos_change, window_size)
            loss_average = SimpleMovingAverage.calculate_moving_average(neg_change, window_size)

        # RSn = gain_average_n/loss_average_n, RSIn = 100 - 100/(1+RSn)
        rsi = []
        for i in range(0, len(gain_average)):
            if gain_average[i] == 0:
                rsi.append(0)           # when average gain = 0 -> rsi = 0
            elif loss_average[i] == 0:
                rsi.append(100)         # when average loss = 0 -> rsi = 100
            else:
                rsi.append(100 - 100/(1+gain_average[i]/loss_average[i]))

        return rsi
    
    """
        calculate the period list
        @param: period_list: datetime list
        @param: window_size: moving average window size
        @return: modified period_list
    """
    def calculate_period_list(self, period_list, window_size=14, rs_type="SMMA") -> list:
        assert len(period_list) > window_size, "list size must be more than window_size"
        assert window_size > 1, "window_size must be more than 1"

        if rs_type == "SMA":
            return period_list[window_size:]
        
        return period_list[1:]
