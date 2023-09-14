import sys
from poker_test import PokerTest
from file_Manager import FileManager
from average_test import AverageTest
from variance_test import VarianceTest
from ks_test import KsTest
#from chi2_test import Chi2Test

class Presenter:
    def __init__(self,):
        self.file_manager = FileManager()
        self.ri_numbers = []
        self.poker_test = PokerTest(self.ri_numbers)
        self.average_test = AverageTest(self.ri_numbers)
        self.variance_test = VarianceTest(self.ri_numbers)
        self.ks_test = KsTest(self.ri_numbers)
        self.view = None  # Esta será la referencia a la ventana principal

    def do_poker_test(self):
        self.poker_test.ri_nums = self.ri_numbers
        self.poker_test.check_poker()
        
    def do_average_test(self):
        self.average_test.ri_numbers = self.ri_numbers
        self.average_test.checkTest()
    
    def do_variance_test(self):
        self.variance_test.ri_numbers = self.ri_numbers
        self.variance_test.checkTest()
    
    def do_variance_test(self):
        self.variance_test.ri_numbers = self.ri_numbers
        self.variance_test.checkTest()
    
    def do_chi2_test(self):
        pass
    
    def do_ks_test(self):
        self.ks_test.ri_numbers = self.ri_numbers
        self.ks_test.checkTest()
    
    def set_main_window(self, main_window):
        self.view = main_window
        
    def add_numbers(self):
        self.ri_numbers = self.file_manager.numbers

    def run(self):
        self.view.show()
        sys.exit(self.app.exec())
