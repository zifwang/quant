import unittest
import numpy as np

from test_utillity.file_reader import FileReader
from src.entity.stock_price_holder import StockPriceHolder
from src.indicator.simple_moving_average import SimpleMovingAverage

def calculate_sma(stock_price_holder = StockPriceHolder, window_size = int):
    close_list = stock_price_holder.get_close_list()
    sma_list = []

    for i in range(0, len(close_list)-window_size+1):
        sum = 0
        for num in close_list[i:i+window_size]:
            sum += num
        
        sma_list.append(round(sum/window_size,4))

    return sma_list

class TestSMA(unittest.TestCase):
    def test_win_size_5(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 5
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        sma = SimpleMovingAverage(stock_price_holder, window_size)
        sma_wait_test = []
        for num in sma.get_moving_average_list():
            sma_wait_test.append(float("{:.4f}".format(num)))
        sma_list_right = calculate_sma(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1: ]

        self.assertAlmostEqual(sma.get_ma_type(), "Simple Moving Average")
        self.assertEqual(sma_wait_test, sma_list_right)
        self.assertEqual(sma.get_period_list(), period_list)
    
    def test_win_size_3(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 3
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        sma = SimpleMovingAverage(stock_price_holder, window_size)
        sma_wait_test = []
        for num in sma.get_moving_average_list():
            sma_wait_test.append(float("{:.4f}".format(num)))
        sma_list_right = calculate_sma(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1: ]

        self.assertAlmostEqual(sma.get_ma_type(), "Simple Moving Average")
        self.assertEqual(sma_wait_test, sma_list_right)
        self.assertEqual(sma.get_period_list(), period_list)
        
    def test_win_size_6(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 3
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        sma = SimpleMovingAverage(stock_price_holder, window_size)
        sma_wait_test = []
        for num in sma.get_moving_average_list():
            sma_wait_test.append(float("{:.4f}".format(num)))
        sma_list_right = calculate_sma(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1: ]

        self.assertAlmostEqual(sma.get_ma_type(), "Simple Moving Average")
        self.assertEqual(sma_wait_test, sma_list_right)
        self.assertEqual(sma.get_period_list(), period_list)
    
    def test_win_size_10(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 3
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        sma = SimpleMovingAverage(stock_price_holder, window_size)
        sma_wait_test = []
        for num in sma.get_moving_average_list():
            sma_wait_test.append(float("{:.4f}".format(num)))
        sma_list_right = calculate_sma(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1: ]

        self.assertAlmostEqual(sma.get_ma_type(), "Simple Moving Average")
        self.assertEqual(sma_wait_test, sma_list_right)
        self.assertEqual(sma.get_period_list(), period_list)
    
    def test_win_size_20(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 3
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        sma = SimpleMovingAverage(stock_price_holder, window_size)
        sma_wait_test = []
        for num in sma.get_moving_average_list():
            sma_wait_test.append(float("{:.4f}".format(num)))
        sma_list_right = calculate_sma(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1: ]

        self.assertAlmostEqual(sma.get_ma_type(), "Simple Moving Average")
        self.assertEqual(sma_wait_test, sma_list_right)
        self.assertEqual(sma.get_period_list(), period_list)

    def test_MSFT_size_20(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 3
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        sma = SimpleMovingAverage(stock_price_holder, window_size)
        sma_wait_test = []
        for num in sma.get_moving_average_list():
            sma_wait_test.append(float("{:.4f}".format(num)))
        sma_list_right = calculate_sma(stock_price_holder, window_size)
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size-1: ]

        self.assertAlmostEqual(sma.get_ma_type(), "Simple Moving Average")
        self.assertEqual(sma_wait_test, sma_list_right)
        self.assertEqual(sma.get_period_list(), period_list)
    
    def test_wsft_win_size_less_than_1_sts_method(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = -1
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        with self.assertRaises(Exception) as context:
            sma = SimpleMovingAverage.calculate_moving_average(stock_price_holder.get_close_list(), window_size)
        
        self.assertAlmostEqual(str(context.exception), "window_size must be more than 1")
