import unittest
import pandas as pd
import numpy as np

from test_utillity.file_reader import FileReader
from src.entity.stock_price_holder import StockPriceHolder
from src.indicator.relative_strength_index import RelativeStrengthIndex

def calculate_rsi(over: pd.Series, fn_roll, length) -> pd.Series:
    # Get the difference in price from previous step
    delta = over.diff()
    # Get rid of the first row, which is NaN since it did not have a previous row to calculate the differences
    delta = delta[1:] 

    # Make the positive gains (up) and negative gains (down) Series
    up, down = delta.clip(lower=0), delta.clip(upper=0).abs()

    roll_up, roll_down = fn_roll(up), fn_roll(down)
    rs = roll_up / roll_down
    rsi = 100.0 - (100.0 / (1.0 + rs))

    # Avoid division-by-zero if `roll_down` is zero
    # This prevents inf and/or nan values.
    rsi[:] = np.select([roll_down == 0, roll_up == 0, True], [100, 0, rsi])
    rsi.name = 'rsi'

    # Assert range
    valid_rsi = rsi[length - 1:]
    assert ((0 <= valid_rsi) & (valid_rsi <= 100)).all()
    # Note: rsi[:length - 1] is excluded from above assertion because it is NaN for SMA.

    return rsi

class TestRSI(unittest.TestCase):
    def test_win_size_5_default(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 5
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        rsi = RelativeStrengthIndex(stock_price_holder,window_size)
        rsi_period_test = rsi.get_period_list()
        rsi_wait_test = rsi.get_rsi_list()
        rsi_test_list = []
        for num in rsi_wait_test:
            rsi_test_list.append(float("{:.4f}".format(num)))

        close = pd.Series(data=stock_price_holder.get_close_list())
        rsi_list = calculate_rsi(close, lambda s: s.ewm(alpha=1/window_size, adjust=False).mean(), window_size)
        rsi_list_right = []
        for rsi in rsi_list:
            rsi_list_right.append(float("{:.4f}".format(rsi)))
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[1:]

        self.assertEqual(rsi_period_test, period_list)
        self.assertEqual(len(rsi_test_list), len(period_list))
        self.assertEqual(rsi_test_list, rsi_list_right)
    
    def test_win_size_14_default(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 14
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        rsi = RelativeStrengthIndex(stock_price_holder,window_size)
        rsi_period_test = rsi.get_period_list()
        rsi_wait_test = rsi.get_rsi_list()
        rsi_test_list = []
        for num in rsi_wait_test:
            rsi_test_list.append(float("{:.4f}".format(num)))

        close = pd.Series(data=stock_price_holder.get_close_list())
        rsi_list = calculate_rsi(close, lambda s: s.ewm(alpha=1/window_size, adjust=False).mean(), window_size)
        rsi_list_right = []
        for rsi in rsi_list:
            rsi_list_right.append(float("{:.4f}".format(rsi)))
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[1:]

        self.assertEqual(rsi_period_test, period_list)
        self.assertEqual(len(rsi_test_list), len(period_list))
        self.assertEqual(rsi_test_list, rsi_list_right)

    def test_win_size_26_default(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 26
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        rsi = RelativeStrengthIndex(stock_price_holder,window_size)
        rsi_period_test = rsi.get_period_list()
        rsi_wait_test = rsi.get_rsi_list()
        rsi_test_list = []
        for num in rsi_wait_test:
            rsi_test_list.append(float("{:.4f}".format(num)))

        close = pd.Series(data=stock_price_holder.get_close_list())
        rsi_list = calculate_rsi(close, lambda s: s.ewm(alpha=1/window_size, adjust=False).mean(), window_size)
        rsi_list_right = []
        for rsi in rsi_list:
            rsi_list_right.append(float("{:.4f}".format(rsi)))
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[1:]

        self.assertEqual(rsi_period_test, period_list)
        self.assertEqual(len(rsi_test_list), len(period_list))
        self.assertEqual(rsi_test_list, rsi_list_right)

    def test_win_size_50_default(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 50
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        rsi = RelativeStrengthIndex(stock_price_holder,window_size)
        rsi_period_test = rsi.get_period_list()
        rsi_wait_test = rsi.get_rsi_list()
        rsi_test_list = []
        for num in rsi_wait_test:
            rsi_test_list.append(float("{:.4f}".format(num)))

        close = pd.Series(data=stock_price_holder.get_close_list())
        rsi_list = calculate_rsi(close, lambda s: s.ewm(alpha=1/window_size, adjust=False).mean(), window_size)
        rsi_list_right = []
        for rsi in rsi_list:
            rsi_list_right.append(float("{:.4f}".format(rsi)))
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[1:]

        self.assertEqual(rsi_period_test, period_list)
        self.assertEqual(len(rsi_test_list), len(period_list))
        self.assertEqual(rsi_test_list, rsi_list_right)
    
    def test_win_size_5_ema(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 5
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        rsi = RelativeStrengthIndex(stock_price_holder,window_size, "EMA")
        rsi_period_test = rsi.get_period_list()
        rsi_wait_test = rsi.get_rsi_list()
        rsi_test_list = []
        for num in rsi_wait_test:
            rsi_test_list.append(float("{:.4f}".format(num)))

        close = pd.Series(data=stock_price_holder.get_close_list())
        rsi_list = calculate_rsi(close, lambda s: s.ewm(span=window_size, adjust=False).mean(), window_size)
        rsi_list_right = []
        for rsi in rsi_list:
            rsi_list_right.append(float("{:.4f}".format(rsi)))
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[1:]

        self.assertEqual(rsi_period_test, period_list)
        self.assertEqual(len(rsi_test_list), len(period_list))
        self.assertEqual(rsi_test_list, rsi_list_right)
    
    def test_win_size_14_ema(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 14
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        rsi = RelativeStrengthIndex(stock_price_holder,window_size, "EMA")
        rsi_period_test = rsi.get_period_list()
        rsi_wait_test = rsi.get_rsi_list()
        rsi_test_list = []
        for num in rsi_wait_test:
            rsi_test_list.append(float("{:.4f}".format(num)))

        close = pd.Series(data=stock_price_holder.get_close_list())
        rsi_list = calculate_rsi(close, lambda s: s.ewm(span=window_size, adjust=False).mean(), window_size)
        rsi_list_right = []
        for rsi in rsi_list:
            rsi_list_right.append(float("{:.4f}".format(rsi)))
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[1:]

        self.assertEqual(rsi_period_test, period_list)
        self.assertEqual(len(rsi_test_list), len(period_list))
        self.assertEqual(rsi_test_list, rsi_list_right)

    def test_win_size_26_ema(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 26
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        rsi = RelativeStrengthIndex(stock_price_holder,window_size, "EMA")
        rsi_period_test = rsi.get_period_list()
        rsi_wait_test = rsi.get_rsi_list()
        rsi_test_list = []
        for num in rsi_wait_test:
            rsi_test_list.append(float("{:.4f}".format(num)))

        close = pd.Series(data=stock_price_holder.get_close_list())
        rsi_list = calculate_rsi(close, lambda s: s.ewm(span=window_size, adjust=False).mean(), window_size)
        rsi_list_right = []
        for rsi in rsi_list:
            rsi_list_right.append(float("{:.4f}".format(rsi)))
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[1:]

        self.assertEqual(rsi_period_test, period_list)
        self.assertEqual(len(rsi_test_list), len(period_list))
        self.assertEqual(rsi_test_list, rsi_list_right)

    def test_win_size_50_ema(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 50
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        rsi = RelativeStrengthIndex(stock_price_holder,window_size, "EMA")
        rsi_period_test = rsi.get_period_list()
        rsi_wait_test = rsi.get_rsi_list()
        rsi_test_list = []
        for num in rsi_wait_test:
            rsi_test_list.append(float("{:.4f}".format(num)))

        close = pd.Series(data=stock_price_holder.get_close_list())
        rsi_list = calculate_rsi(close, lambda s: s.ewm(span=window_size, adjust=False).mean(), window_size)
        rsi_list_right = []
        for rsi in rsi_list:
            rsi_list_right.append(float("{:.4f}".format(rsi)))
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[1:]

        self.assertEqual(rsi_period_test, period_list)
        self.assertEqual(len(rsi_test_list), len(period_list))
        self.assertEqual(rsi_test_list, rsi_list_right)

    def test_win_size_5_sma(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 5
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        rsi = RelativeStrengthIndex(stock_price_holder,window_size, "SMA")
        rsi_period_test = rsi.get_period_list()
        rsi_wait_test = rsi.get_rsi_list()
        rsi_test_list = []
        for num in rsi_wait_test:
            rsi_test_list.append(float("{:.4f}".format(num)))

        close = pd.Series(data=stock_price_holder.get_close_list())
        rsi_list = calculate_rsi(close, lambda s: s.rolling(window_size).mean(), window_size)
        rsi_list_right = []
        for rsi in rsi_list:
            if np.isnan(rsi):
                continue
            rsi_list_right.append(float("{:.4f}".format(rsi)))
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size:]

        self.assertEqual(rsi_period_test, period_list)
        self.assertEqual(len(rsi_test_list), len(period_list))
        self.assertEqual(rsi_test_list, rsi_list_right)
    
    def test_win_size_14_sma(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 14
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        rsi = RelativeStrengthIndex(stock_price_holder,window_size, "SMA")
        rsi_period_test = rsi.get_period_list()
        rsi_wait_test = rsi.get_rsi_list()
        rsi_test_list = []
        for num in rsi_wait_test:
            rsi_test_list.append(float("{:.4f}".format(num)))

        close = pd.Series(data=stock_price_holder.get_close_list())
        rsi_list = calculate_rsi(close, lambda s: s.rolling(window_size).mean(), window_size)
        rsi_list_right = []
        for rsi in rsi_list:
            if np.isnan(rsi):
                continue
            rsi_list_right.append(float("{:.4f}".format(rsi)))
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size:]

        self.assertEqual(rsi_period_test, period_list)
        self.assertEqual(len(rsi_test_list), len(period_list))
        self.assertEqual(rsi_test_list, rsi_list_right)

    def test_win_size_26_sma(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 26
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        rsi = RelativeStrengthIndex(stock_price_holder,window_size, "SMA")
        rsi_period_test = rsi.get_period_list()
        rsi_wait_test = rsi.get_rsi_list()
        rsi_test_list = []
        for num in rsi_wait_test:
            rsi_test_list.append(float("{:.4f}".format(num)))

        close = pd.Series(data=stock_price_holder.get_close_list())
        rsi_list = calculate_rsi(close, lambda s: s.rolling(window_size).mean(), window_size)
        rsi_list_right = []
        for rsi in rsi_list:
            if np.isnan(rsi):
                continue
            rsi_list_right.append(float("{:.4f}".format(rsi)))
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size:]

        self.assertEqual(rsi_period_test, period_list)
        self.assertEqual(len(rsi_test_list), len(period_list))
        self.assertEqual(rsi_test_list, rsi_list_right)

    def test_win_size_50_sma(self):
        stock_name = "Apple"
        stock_no = "AAPL"
        window_size = 50
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_AAPL.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        rsi = RelativeStrengthIndex(stock_price_holder,window_size, "SMA")
        rsi_period_test = rsi.get_period_list()
        rsi_wait_test = rsi.get_rsi_list()
        rsi_test_list = []
        for num in rsi_wait_test:
            rsi_test_list.append(float("{:.4f}".format(num)))

        close = pd.Series(data=stock_price_holder.get_close_list())
        rsi_list = calculate_rsi(close, lambda s: s.rolling(window_size).mean(), window_size)
        rsi_list_right = []
        for rsi in rsi_list:
            if np.isnan(rsi):
                continue
            rsi_list_right.append(float("{:.4f}".format(rsi)))
        period_list = stock_price_holder.get_date_list()
        period_list = period_list[window_size:]

        self.assertEqual(rsi_period_test, period_list)
        self.assertEqual(len(rsi_test_list), len(period_list))
        self.assertEqual(rsi_test_list, rsi_list_right)
    
    def test_win_size_more_than_list(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 3000
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        with self.assertRaises(Exception) as context:
            rsi = RelativeStrengthIndex(stock_price_holder, window_size)
        
        self.assertAlmostEqual(str(context.exception), "list size must be more than window_size")
    
    def test_wsft_rs_type_not_fit(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = 14
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        with self.assertRaises(Exception) as context:
            rsi = RelativeStrengthIndex(stock_price_holder, window_size, "CMA")
        
        self.assertAlmostEqual(str(context.exception), "RSI calculation only support SMMA, EMA, and SMA")

    def test_wsft_win_size_less_than_0(self):
        stock_name = "MicroSoft"
        stock_no = "MSFT"
        window_size = -1
        file_name = "C:/Users/insan/Documents/Project/Python/Project/quant/test/test_data/HistoricalData_MSFT.csv"
        file_reader = FileReader(file_name)
        stock_price_holder = file_reader.read_csv_file_to_stock_price_holder(stock_name, stock_no)

        with self.assertRaises(Exception) as context:
            rsi = RelativeStrengthIndex.rsi(stock_price_holder.get_close_list(), window_size, "SMA")
        
        self.assertAlmostEqual(str(context.exception), "window_size must be more than 1")

