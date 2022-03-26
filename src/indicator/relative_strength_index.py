import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from entity.stock_price_holder import StockPriceHolder

class RelativeStrengthIndex:
    def __init__(self, stock_price_holder = StockPriceHolder, window_size = 14, ):