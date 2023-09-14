import sys
from poker_test import PokerTest
from file_Manager import FileManager
#from chi2_test import Chi2Test
#from ks_test import KSTest

class Presenter:
    def __init__(self,):
        self.file_manager = FileManager()
        self.ri_numbers = []
        self.poker_test = PokerTest(self.ri_numbers)
        self.view = None  # Esta será la referencia a la ventana principal

    def do_poker_test(self):
        self.poker_test.ri_nums = self.ri_numbers
        self.poker_test.check_poker()
        
    def do_average_test(self):
        pass
    
    def do_variance_test(self):
        pass
    
    def do_chi2_test(self):
        pass
    
    def do_ks_test(self):
        pass
    
    def set_main_window(self, main_window):
        self.view = main_window
        
    def add_numbers(self):
        self.ri_numbers = self.file_manager.numbers

    def run(self):
        self.view.show()
        sys.exit(self.app.exec())
