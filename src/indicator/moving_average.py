from entity.stock_price_holder import StockPriceHolder

class MovingAverage:
    def __init__(self, stock_price_holder = StockPriceHolder, window_size = int, ma_type = str):
        self.stock_price_holder = stock_price_holder
        self.ma_type = ma_type
        self.window_size = window_size
        self.moving_average_list = []
        self.period_list = []

    def calculate_moving_average(self) -> None:
        raise NotImplementedError
        
    """
        Below is getter and setter setcion
    """
    def set_stock_price_holder(self, stock_price_holder = StockPriceHolder) -> None:
        self.stock_price_holder = stock_price_holder
    def get_stock_price_holder(self) -> StockPriceHolder:
        return self.stock_price_holder

    def set_ma_type(self, ma_type = str) -> None:
        self.ma_type = ma_type
    def get_ma_type(self) -> str:
        return self.ma_type

    def set_window_size(self, window_size) -> None:
        self.window_size = window_size
    def get_window_size(self) -> int:
        return self.window_size
    
    def get_moving_average_list(self) -> list:
        return self.moving_average_list
    
    def get_period_list(self) -> list:
        return self.period_list

    """ 
        to_string method to format stock entity into a readable format
        @param: not required
        @return: MovingAverage entity in a readable format string
    """
    def to_string(self):
        periods = self.period_list[0] + "--" + self.period_list[len(self.period_list)-1]
        stock_info = self.stock_price_holder.get_stock_name() + "(" + self.stock_price_holder.get_stock_no + ")"
        ma = self.moving_average_list[0] + self.moving_average_list[1] + self.moving_average_list[2] + "..."

        return '[stock:{stock_info}, moving_average_type:{ma_type}, period:{periods}, calculated_moving_average:{ma}]'.format(stock_info=stock_info, ma_type=self.ma_type, periods=periods, ma=ma)