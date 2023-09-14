import sys
from average_test import AverageTest 
from poker_test import PokerTest
from variance_test import VarianceTest
from file_Manager import FileManager
#from chi2_test import Chi2Test
#from ks_test import KSTest

class Presenter:
    def __init__(self,):
        self.file_manager = FileManager()
        self.ri_numbers = []
        self.view = None  # Esta será la referencia a la ventana principal

    def set_main_window(self, main_window):
        self.view = main_window
        
    def add_numbers(self):
        self.ri_numbers = self.file_manager.numbers

    def run(self):
        self.view.show()
        sys.exit(self.app.exec())
