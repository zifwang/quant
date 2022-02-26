import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import csv
from datetime import datetime
from src.entity.stock_price import StockPrice
from src.entity.stock_price_holder import StockPriceHolder

class FileReader:
    def __init__(self, file_name = str):
        self.file_name = file_name
    
    def read_csv_file_to_stock_price_list(self, stock_name = str, stock_no = str) -> list:
        assert '.csv' in self.file_name, "file should be endding with .csv" 

        stock_price_list = []
        with open(self.file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader) #skip header

            for row in csv_reader:
                stock_price = StockPrice(stock_name, stock_no)
                for i in range(0, len(row)):
                    if i == 0:
                        # date
                        date = row[i].split("/")
                        stock_price.set_datetime(datetime(int(date[2]),int(date[0]),int(date[1])))
                    
                    if i == 1:
                        # close price
                        stock_price.set_close_price(float(row[i][1:]))

                    if i == 2:
                        # volume
                        stock_price.set_volume(int(row[i]))
                    
                    if i == 3:
                        # open
                        stock_price.set_open_price(float(row[i][1:]))

                    if i == 4:
                        # high
                        stock_price.set_high_price(float(row[i][1:]))

                    if i == 5:
                        # low
                        stock_price.set_low_price(float(row[i][1:]))

                stock_price_list.append(stock_price)
        csv_file.close()
        stock_price_list.reverse()

        return stock_price_list
    
    def read_csv_file_to_stock_price_holder(self, stock_name = str, stock_no = str) -> StockPriceHolder:
        price_list = self.read_csv_file_to_stock_price_list(stock_name, stock_no)
        open_list = []
        closed_list = []
        high_list = []
        low_list = []
        volume_list = []
        date_list = []
        for i in range(0, len(price_list)):
            open_list.append(price_list[i].open_price)
            closed_list.append(price_list[i].close_price)
            high_list.append(price_list[i].high_price)
            low_list.append(price_list[i].low_price)
            volume_list.append(price_list[i].volume)
            date_list.append(price_list[i].dateTime)
        
        return StockPriceHolder(stock_name, stock_no, open_list, closed_list, high_list, low_list, volume_list, date_list)