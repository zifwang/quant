import unittest
import pandas as pd
import numpy as np

from test_utillity.file_reader import FileReader
from src.entity.stock_price_holder import StockPriceHolder
from src.indicator.bias_ratio import BiasRatio
from src.indicator.simple_moving_average import SimpleMovingAverage

def calculate_br(stock_price_holder = StockPriceHolder, window_size = int):
    close_list = stock_price_holder.get_close_list()
    ma = SimpleMovingAverage.calculate_moving_average(close_list, window_size)
    close_list = close_list[window_size-1:]

    br_list = []
    for i in range(0,len(close_list)):
        br = (close_list[i] - ma[i])/ma[i]
        br_list.append(float("{:.4f}".format(br)))
    
    return br_list

class TestBR(unittest.TestCase):
    def test_win_size_5(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 5
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        br = BiasRatio(stock_price_holder,window_size)
        br_wait_test = br.get_bias_ratio()
        br_test_list = []
        for num in br_wait_test:
            br_test_list.append(float("{:.4f}".format(num)))

        br_list_right = calculate_br(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertEqual(br.get_period_list(), period_list)
        self.assertEqual(len(br_test_list), len(period_list))
        self.assertEqual(br_test_list, br_list_right)

    def test_win_size_9(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 9
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        br = BiasRatio(stock_price_holder,window_size)
        br_wait_test = br.get_bias_ratio()
        br_test_list = []
        for num in br_wait_test:
            br_test_list.append(float("{:.4f}".format(num)))

        br_list_right = calculate_br(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertEqual(br.get_period_list(), period_list)
        self.assertEqual(len(br_test_list), len(period_list))
        self.assertEqual(br_test_list, br_list_right)

    def test_win_size_12(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 12
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        br = BiasRatio(stock_price_holder,window_size)
        br_wait_test = br.get_bias_ratio()
        br_test_list = []
        for num in br_wait_test:
            br_test_list.append(float("{:.4f}".format(num)))

        br_list_right = calculate_br(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertEqual(br.get_period_list(), period_list)
        self.assertEqual(len(br_test_list), len(period_list))
        self.assertEqual(br_test_list, br_list_right)

    def test_win_size_26(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 26
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        br = BiasRatio(stock_price_holder,window_size)
        br_wait_test = br.get_bias_ratio()
        br_test_list = []
        for num in br_wait_test:
            br_test_list.append(float("{:.4f}".format(num)))

        br_list_right = calculate_br(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertEqual(br.get_period_list(), period_list)
        self.assertEqual(len(br_test_list), len(period_list))
        self.assertEqual(br_test_list, br_list_right)

    def test_msft_win_5(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 5
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        br = BiasRatio(stock_price_holder,window_size)
        br_wait_test = br.get_bias_ratio()
        br_test_list = []
        for num in br_wait_test:
            br_test_list.append(float("{:.4f}".format(num)))

        br_list_right = calculate_br(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertEqual(br.get_period_list(), period_list)
        self.assertEqual(len(br_test_list), len(period_list))
        self.assertEqual(br_test_list, br_list_right)

    def test_msft_win_9(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 9
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        br = BiasRatio(stock_price_holder,window_size)
        br_wait_test = br.get_bias_ratio()
        br_test_list = []
        for num in br_wait_test:
            br_test_list.append(float("{:.4f}".format(num)))

        br_list_right = calculate_br(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertEqual(br.get_period_list(), period_list)
        self.assertEqual(len(br_test_list), len(period_list))
        self.assertEqual(br_test_list, br_list_right)

    def test_msft_win_12(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 12
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        br = BiasRatio(stock_price_holder,window_size)
        br_wait_test = br.get_bias_ratio()
        br_test_list = []
        for num in br_wait_test:
            br_test_list.append(float("{:.4f}".format(num)))

        br_list_right = calculate_br(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertEqual(br.get_period_list(), period_list)
        self.assertEqual(len(br_test_list), len(period_list))
        self.assertEqual(br_test_list, br_list_right)

    def test_msft_win_26(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 26
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        br = BiasRatio(stock_price_holder,window_size)
        br_wait_test = br.get_bias_ratio()
        br_test_list = []
        for num in br_wait_test:
            br_test_list.append(float("{:.4f}".format(num)))

        br_list_right = calculate_br(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertEqual(br.get_period_list(), period_list)
        self.assertEqual(len(br_test_list), len(period_list))
        self.assertEqual(br_test_list, br_list_right)