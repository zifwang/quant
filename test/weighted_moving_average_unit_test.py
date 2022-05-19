import unittest
import pandas as pd
import numpy as np

from test_utillity.file_reader import FileReader
from src.entity.stock_price_holder import StockPriceHolder
from src.indicator.weighted_moving_average import WeightedMovingAverage

def calculate_wma_by_pandas(stock_price_holder = StockPriceHolder, window_size=int):
    close_list = stock_price_holder.get_close_list()
    weights = np.arange(1, window_size + 1)
    df = pd.DataFrame({'val': close_list})
    wmas = df['val'].rolling(window_size).apply(lambda x: np.dot(x, weights) /
                                       weights.sum()).to_list()

    ans_list = []
    for num in wmas:
        ans_list.append(float("{:.4f}".format(num)))

    return ans_list[window_size-1:]

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
        
        wma_list_right = calculate_wma_by_pandas(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(wma.get_ma_type(), "Weighted Moving Average")
        self.assertEqual(wma_test_list, wma_list_right)
        self.assertEqual(wma.get_period_list(), period_list)
        self.assertEqual(len(wma_test_list), len(period_list))

    def test_appl_win_9(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 9
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        wma = WeightedMovingAverage(stock_price_holder, window_size)
        wma_wait_test = wma.get_moving_average_list()
        wma_test_list = []
        for num in wma_wait_test:
            wma_test_list.append(float("{:.4f}".format(num)))
        
        wma_list_right = calculate_wma_by_pandas(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(wma.get_ma_type(), "Weighted Moving Average")
        self.assertEqual(wma_test_list, wma_list_right)
        self.assertEqual(wma.get_period_list(), period_list)
        self.assertEqual(len(wma_test_list), len(period_list))
    
    def test_appl_win_12(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 12
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        wma = WeightedMovingAverage(stock_price_holder, window_size)
        wma_wait_test = wma.get_moving_average_list()
        wma_test_list = []
        for num in wma_wait_test:
            wma_test_list.append(float("{:.4f}".format(num)))
        
        wma_list_right = calculate_wma_by_pandas(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(wma.get_ma_type(), "Weighted Moving Average")
        self.assertEqual(wma_test_list, wma_list_right)
        self.assertEqual(wma.get_period_list(), period_list)
        self.assertEqual(len(wma_test_list), len(period_list))
    
    def test_appl_win_26(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 26
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        wma = WeightedMovingAverage(stock_price_holder, window_size)
        wma_wait_test = wma.get_moving_average_list()
        wma_test_list = []
        for num in wma_wait_test:
            wma_test_list.append(float("{:.4f}".format(num)))
        
        wma_list_right = calculate_wma_by_pandas(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(wma.get_ma_type(), "Weighted Moving Average")
        self.assertEqual(wma_test_list, wma_list_right)
        self.assertEqual(wma.get_period_list(), period_list)
        self.assertEqual(len(wma_test_list), len(period_list))
    
    def test_msft_win_5(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 5
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        wma = WeightedMovingAverage(stock_price_holder, window_size)
        wma_wait_test = wma.get_moving_average_list()
        wma_test_list = []
        for num in wma_wait_test:
            wma_test_list.append(float("{:.4f}".format(num)))
        
        wma_list_right = calculate_wma_by_pandas(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(wma.get_ma_type(), "Weighted Moving Average")
        self.assertEqual(wma_test_list, wma_list_right)
        self.assertEqual(wma.get_period_list(), period_list)
        self.assertEqual(len(wma_test_list), len(period_list))    

    def test_msft_win_9(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 9
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        wma = WeightedMovingAverage(stock_price_holder, window_size)
        wma_wait_test = wma.get_moving_average_list()
        wma_test_list = []
        for num in wma_wait_test:
            wma_test_list.append(float("{:.4f}".format(num)))
        
        wma_list_right = calculate_wma_by_pandas(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(wma.get_ma_type(), "Weighted Moving Average")
        self.assertEqual(wma_test_list, wma_list_right)
        self.assertEqual(wma.get_period_list(), period_list)
        self.assertEqual(len(wma_test_list), len(period_list))        
    
    def test_msft_win_12(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 12
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        wma = WeightedMovingAverage(stock_price_holder, window_size)
        wma_wait_test = wma.get_moving_average_list()
        wma_test_list = []
        for num in wma_wait_test:
            wma_test_list.append(float("{:.4f}".format(num)))
        
        wma_list_right = calculate_wma_by_pandas(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(wma.get_ma_type(), "Weighted Moving Average")
        self.assertEqual(wma_test_list, wma_list_right)
        self.assertEqual(wma.get_period_list(), period_list)
        self.assertEqual(len(wma_test_list), len(period_list))     
    
    def test_msft_win_26(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 26
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        wma = WeightedMovingAverage(stock_price_holder, window_size)
        wma_wait_test = wma.get_moving_average_list()
        wma_test_list = []
        for num in wma_wait_test:
            wma_test_list.append(float("{:.4f}".format(num)))
        
        wma_list_right = calculate_wma_by_pandas(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1:]

        self.assertAlmostEqual(wma.get_ma_type(), "Weighted Moving Average")
        self.assertEqual(wma_test_list, wma_list_right)
        self.assertEqual(wma.get_period_list(), period_list)
        self.assertEqual(len(wma_test_list), len(period_list))     
    
    def test_wsft_win_size_less_than_1_sts_method(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = -1
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        with self.assertRaises(Exception) as context:
            wma = WeightedMovingAverage.calculate_moving_average(stock_price_holder.get_close_list(), window_size)
        
        self.assertAlmostEqual(str(context.exception), "window_size must be more than 1")
