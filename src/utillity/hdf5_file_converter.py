import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import h5py

class Hdf5FileConverter:
    def __init__(self, file_path = None):
        self.file_path = file_path
     
    def convert_hdf5_to_stock_price(self):
        assert '.h5' in self.file_path, "file_path should end with .h5"

        with h5py.File(self.file_path, 'r') as hdf5_file:
        