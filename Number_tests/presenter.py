import sys
from PyQt6.QtWidgets import QApplication
from view import MainWindow  # Importa la clase MainWindow desde la ubicación correcta
from average_test import AverageTest 
from poker_test import PokerTest
from variance_test import VarianceTest
from file_Manager import File_Manager
#from chi2_test import Chi2Test
#from ks_test import KSTest

class Presenter:
    def __init__(self):
        self.ri_numbers = []
        self.poker_test = None
        self.variance_test = None
        self.average_test = None
        self.chi2_test = None
        self.ks_test = None
        self.file_manager = File_Manager()
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()

    def create_tests(self):
        if(self.ri_numbers != []):
            self.poker_test = PokerTest(self.ri_numbers)
            self.variance_test = VarianceTest(self.ri_numbers)
            self.average_test = AverageTest(self.ri_numbers)

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec())
