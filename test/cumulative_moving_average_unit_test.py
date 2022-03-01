from fileinput import close
import unittest
import pandas as pd
import numpy as np

from test_utillity.file_reader import FileReader
from src.entity.stock_price_holder import StockPriceHolder
from src.indicator.cumulative_moving_average import CumulativeMovingAverage

def calculate_cma_by_panads(stock_price_holder = StockPriceHolder, window_size = int):
    close_list = stock_price_holder.get_close_list()
    df = pd.DataFrame({'val': close_list})
    cma_list = df.expanding(min_periods=window_size).mean()
    cma_list = list(cma_list['val'])
    cma_list = cma_list[window_size-1:]

    ans_list = []
    for num in cma_list:
        ans_list.append(float("{:.3f}".format(num)))

    return ans_list

class TestCMA(unittest.TestCase):
    def test_aapl_win_5(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 5
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        cma = CumulativeMovingAverage(stock_price_holder, window_size)
        cma_wait_test = cma.get_moving_average_list()
        cma_test_list = []
        for num in cma_wait_test:
            cma_test_list.append(float("{:.3f}".format(num)))

        cma_list_right = calculate_cma_by_panads(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(cma.get_ma_type(), "Cumulative Moving Average")
        self.assertEqual(cma.get_period_list(), period_list)
        self.assertEqual(len(cma_test_list), len(period_list))
        self.assertEqual(cma_test_list, cma_list_right)

    def test_aapl_win_9(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 9
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        cma = CumulativeMovingAverage(stock_price_holder, window_size)
        cma_wait_test = cma.get_moving_average_list()
        cma_test_list = []
        for num in cma_wait_test:
            cma_test_list.append(float("{:.3f}".format(num)))

        cma_list_right = calculate_cma_by_panads(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(cma.get_ma_type(), "Cumulative Moving Average")
        self.assertEqual(cma.get_period_list(), period_list)
        self.assertEqual(len(cma_test_list), len(period_list))
        self.assertEqual(cma_test_list, cma_list_right)

    def test_aapl_win_12(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 12
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        cma = CumulativeMovingAverage(stock_price_holder, window_size)
        cma_wait_test = cma.get_moving_average_list()
        cma_test_list = []
        for num in cma_wait_test:
            cma_test_list.append(float("{:.3f}".format(num)))

        cma_list_right = calculate_cma_by_panads(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(cma.get_ma_type(), "Cumulative Moving Average")
        self.assertEqual(cma.get_period_list(), period_list)
        self.assertEqual(len(cma_test_list), len(period_list))
        self.assertEqual(cma_test_list, cma_list_right)

    def test_aapl_win_26(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 12
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        cma = CumulativeMovingAverage(stock_price_holder, window_size)
        cma_wait_test = cma.get_moving_average_list()
        cma_test_list = []
        for num in cma_wait_test:
            cma_test_list.append(float("{:.3f}".format(num)))

        cma_list_right = calculate_cma_by_panads(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(cma.get_ma_type(), "Cumulative Moving Average")
        self.assertEqual(cma.get_period_list(), period_list)
        self.assertEqual(len(cma_test_list), len(period_list))
        self.assertEqual(cma_test_list, cma_list_right)

    def test_msft_win_5(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 5
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        cma = CumulativeMovingAverage(stock_price_holder, window_size)
        cma_wait_test = cma.get_moving_average_list()
        cma_test_list = []
        for num in cma_wait_test:
            cma_test_list.append(float("{:.3f}".format(num)))

        cma_list_right = calculate_cma_by_panads(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(cma.get_ma_type(), "Cumulative Moving Average")
        self.assertEqual(cma.get_period_list(), period_list)
        self.assertEqual(len(cma_test_list), len(period_list))
        self.assertEqual(cma_test_list, cma_list_right)

    def test_msft_win_9(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 9
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        cma = CumulativeMovingAverage(stock_price_holder, window_size)
        cma_wait_test = cma.get_moving_average_list()
        cma_test_list = []
        for num in cma_wait_test:
            cma_test_list.append(float("{:.3f}".format(num)))

        cma_list_right = calculate_cma_by_panads(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(cma.get_ma_type(), "Cumulative Moving Average")
        self.assertEqual(cma.get_period_list(), period_list)
        self.assertEqual(len(cma_test_list), len(period_list))
        self.assertEqual(cma_test_list, cma_list_right)

    def test_msft_win_12(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 12
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        cma = CumulativeMovingAverage(stock_price_holder, window_size)
        cma_wait_test = cma.get_moving_average_list()
        cma_test_list = []
        for num in cma_wait_test:
            cma_test_list.append(float("{:.3f}".format(num)))

        cma_list_right = calculate_cma_by_panads(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(cma.get_ma_type(), "Cumulative Moving Average")
        self.assertEqual(cma.get_period_list(), period_list)
        self.assertEqual(len(cma_test_list), len(period_list))
        self.assertEqual(cma_test_list, cma_list_right)