import sys
from PyQt6.QtWidgets import QApplication
from view import MainWindow  # Importa la clase MainWindow desde la ubicación correcta
from average_test import AverageTest 
from poker_test import PokerTest
from variance_test import VarianceTest
from file_Manager import FileManager
#from chi2_test import Chi2Test
#from ks_test import KSTest
class Presenter:
    def __init__(self):
        self.ri_numbers = []
        self.poker_test = PokerTest(self.ri_numbers)
        self.variance_test = PokerTest(self.ri_numbers)
        self.average_test = PokerTest(self.ri_numbers)
        self.chi2_test = PokerTest(self.ri_numbers)
        self.ks_test = PokerTest(self.ri_numbers)
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow(self)

    def create_tests(self):
        if self.ri_numbers != []:
            self.poker_test = PokerTest(self.ri_numbers)
            self.variance_test = VarianceTest(self.ri_numbers)
            self.average_test = AverageTest(self.ri_numbers)

    def print(self):
        print("Hola")

    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec())

def main():
    presenter = Presenter()
    presenter.run()

if __name__ == "__main__":
    main()