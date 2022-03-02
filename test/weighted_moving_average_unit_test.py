import unittest
import pandas as pd
import numpy as np

from test_utillity.file_reader import FileReader
from src.entity.stock_price_holder import StockPriceHolder
from src.indicator.weighted_moving_average import WeightedMovingAverage

class TestWMA(unittest.TestCase):
    def test_appl_win_5(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 5
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        wma = WeightedMovingAverage(stock_price_holder, window_size)
        wma_wait_test = wma.get_moving_average_list()
        wma_test_list = []
        for num in wma_wait_test:
            wma_test_list.append(float("{:.4f}".format(num)))