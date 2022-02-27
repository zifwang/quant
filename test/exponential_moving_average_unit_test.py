import unittest
import pandas as pd
import numpy as np

from test_utillity.file_reader import FileReader
from src.entity.stock_price_holder import StockPriceHolder
from src.indicator.exponential_moving_average import ExponentialMovingAverage


def calculate_ema_by_panads(stock_price_holder = StockPriceHolder, window_size = int, alpha = float):
    close_list = stock_price_holder.get_close_list()
    df = pd.DataFrame({'val': close_list})
    ema_list = df.ewm(alpha=alpha, adjust=False).mean()
    ema_list = list(ema_list['val'])

    ans_list = []
    for num in ema_list:
        ans_list.append(float("{:.4f}".format(num)))

    return ans_list

class TestEMA(unittest.TestCase):
    def test_aapl_win_5(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 5
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)
        alpha = 2/(1+window_size)

        ema = ExponentialMovingAverage(stock_price_holder, window_size)
        ema_wait_test = ema.get_moving_average_list()
        ema_test_list = []
        for num in ema_wait_test:
            ema_test_list.append(float("{:.4f}".format(num)))

        ema_list_right = calculate_ema_by_panads(stock_price_holder, window_size, alpha)
        period_list = stock_price_holder.get_date_list()

        self.assertAlmostEqual(ema.get_ma_type(), "Exponential Moving Average")
        self.assertEqual(ema_test_list, ema_list_right)
        self.assertEqual(ema.get_period_list(), period_list)
        self.assertEqual(len(ema_test_list), len(period_list))
        self.assertEqual(ema.get_alpha(), alpha)

    def test_aapl_win_9(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 9
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)
        alpha = 2/(1+window_size)

        ema = ExponentialMovingAverage(stock_price_holder, window_size)
        ema_wait_test = ema.get_moving_average_list()
        ema_test_list = []
        for num in ema_wait_test:
            ema_test_list.append(float("{:.4f}".format(num)))

        ema_list_right = calculate_ema_by_panads(stock_price_holder, window_size, alpha)
        period_list = stock_price_holder.get_date_list()

        self.assertAlmostEqual(ema.get_ma_type(), "Exponential Moving Average")
        self.assertEqual(ema_test_list, ema_list_right)
        self.assertEqual(ema.get_period_list(), period_list)
        self.assertEqual(len(ema_test_list), len(period_list))
        self.assertEqual(ema.get_alpha(), alpha)
    
    def test_aapl_win_12(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 12
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)
        alpha = 2/(1+window_size)

        ema = ExponentialMovingAverage(stock_price_holder, window_size)
        ema_wait_test = ema.get_moving_average_list()
        ema_test_list = []
        for num in ema_wait_test:
            ema_test_list.append(float("{:.4f}".format(num)))

        ema_list_right = calculate_ema_by_panads(stock_price_holder, window_size, alpha)
        period_list = stock_price_holder.get_date_list()

        self.assertAlmostEqual(ema.get_ma_type(), "Exponential Moving Average")
        self.assertEqual(ema_test_list, ema_list_right)
        self.assertEqual(ema.get_period_list(), period_list)
        self.assertEqual(len(ema_test_list), len(period_list))
        self.assertEqual(ema.get_alpha(), alpha)

    def test_aapl_win_26(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 26
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)
        alpha = 2/(1+window_size)

        ema = ExponentialMovingAverage(stock_price_holder, window_size)
        ema_wait_test = ema.get_moving_average_list()
        ema_test_list = []
        for num in ema_wait_test:
            ema_test_list.append(float("{:.4f}".format(num)))

        ema_list_right = calculate_ema_by_panads(stock_price_holder, window_size, alpha)
        period_list = stock_price_holder.get_date_list()

        self.assertAlmostEqual(ema.get_ma_type(), "Exponential Moving Average")
        self.assertEqual(ema_test_list, ema_list_right)
        self.assertEqual(ema.get_period_list(), period_list)
        self.assertEqual(len(ema_test_list), len(period_list))
        self.assertEqual(ema.get_alpha(), alpha)
    
    def test_msft_win_5(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 5
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)
        alpha = 2/(1+window_size)

        ema = ExponentialMovingAverage(stock_price_holder, window_size)
        ema_wait_test = ema.get_moving_average_list()
        ema_test_list = []
        for num in ema_wait_test:
            ema_test_list.append(float("{:.4f}".format(num)))

        ema_list_right = calculate_ema_by_panads(stock_price_holder, window_size, alpha)
        period_list = stock_price_holder.get_date_list()

        self.assertAlmostEqual(ema.get_ma_type(), "Exponential Moving Average")
        self.assertEqual(ema_test_list, ema_list_right)
        self.assertEqual(ema.get_period_list(), period_list)
        self.assertEqual(len(ema_test_list), len(period_list))
        self.assertEqual(ema.get_alpha(), alpha)
    
    def test_msft_win_9(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 9
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)
        alpha = 2/(1+window_size)

        ema = ExponentialMovingAverage(stock_price_holder, window_size)
        ema_wait_test = ema.get_moving_average_list()
        ema_test_list = []
        for num in ema_wait_test:
            ema_test_list.append(float("{:.4f}".format(num)))

        ema_list_right = calculate_ema_by_panads(stock_price_holder, window_size, alpha)
        period_list = stock_price_holder.get_date_list()

        self.assertAlmostEqual(ema.get_ma_type(), "Exponential Moving Average")
        self.assertEqual(ema_test_list, ema_list_right)
        self.assertEqual(ema.get_period_list(), period_list)
        self.assertEqual(len(ema_test_list), len(period_list))
        self.assertEqual(ema.get_alpha(), alpha)
    
    def test_msft_win_12(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 12
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)
        alpha = 2/(1+window_size)

        ema = ExponentialMovingAverage(stock_price_holder, window_size)
        ema_wait_test = ema.get_moving_average_list()
        ema_test_list = []
        for num in ema_wait_test:
            ema_test_list.append(float("{:.4f}".format(num)))

        ema_list_right = calculate_ema_by_panads(stock_price_holder, window_size, alpha)
        period_list = stock_price_holder.get_date_list()

        self.assertAlmostEqual(ema.get_ma_type(), "Exponential Moving Average")
        self.assertEqual(ema_test_list, ema_list_right)
        self.assertEqual(ema.get_period_list(), period_list)
        self.assertEqual(len(ema_test_list), len(period_list))
        self.assertEqual(ema.get_alpha(), alpha)

    def test_msft_win_26(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 26
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)
        alpha = 2/(1+window_size)

        ema = ExponentialMovingAverage(stock_price_holder, window_size)
        ema_wait_test = ema.get_moving_average_list()
        ema_test_list = []
        for num in ema_wait_test:
            ema_test_list.append(float("{:.4f}".format(num)))

        ema_list_right = calculate_ema_by_panads(stock_price_holder, window_size, alpha)
        period_list = stock_price_holder.get_date_list()

        self.assertAlmostEqual(ema.get_ma_type(), "Exponential Moving Average")
        self.assertEqual(ema_test_list, ema_list_right)
        self.assertEqual(ema.get_period_list(), period_list)
        self.assertEqual(len(ema_test_list), len(period_list))
        self.assertEqual(ema.get_alpha(), alpha)

    def test_win_size_less_than_2(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 1
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)
        alpha = 2/(1+window_size)

        with self.assertRaises(Exception) as context:
            ema = ExponentialMovingAverage(stock_price_holder, window_size)
        
        self.assertAlmostEqual(str(context.exception), "window size has to more than 1")

    def test_alpha_not_in_range(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 3
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)
        alpha = 2

        with self.assertRaises(Exception) as context:
            ema = ExponentialMovingAverage(stock_price_holder, window_size, alpha)
        
        self.assertAlmostEqual(str(context.exception), "smoothing factor(alpha) is not in the range")

        
    def test_alpha_less_than_0(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 3
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)
        alpha = -1

        with self.assertRaises(Exception) as context:
            ema = ExponentialMovingAverage(stock_price_holder, window_size, alpha)
        
        self.assertAlmostEqual(str(context.exception), "smoothing factor(alpha) is not in the range")