import sys
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QLineEdit, QVBoxLayout, QLabel, QPushButton, QFileDialog
from presenter import Presenter
from poker_test import PokerTest
from average_test import AverageTest
from variance_test import VarianceTest
from ks_test import KsTest
class MainWindow(QMainWindow):
    def __init__(self, presenter):
        super().__init__()
        self.initUI()
        self.presenter = presenter

    def initUI(self):
        self.setWindowTitle("Number tests")
        self.setGeometry(100, 100, 500, 400) 
        tab_widget = QTabWidget()
        self.poker_tab = PokerTab(self)  # Pass a reference to the MainWindow
        self.means_tab = MeansTab(self)
        self.variance_tab = VarianceTab(self)
        tab_widget.addTab(self.poker_tab, "Poker Test")
        tab_widget.addTab(self.means_tab, "Means Test")
        tab_widget.addTab(self.variance_tab, "Variance Test")
        tab_widget.addTab(KsTab(), "K-S Test")
        tab_widget.addTab(ChiTab(), "Chi2 Test")
        vbox = QVBoxLayout()
        vbox.addWidget(tab_widget)
        self.load_button = QPushButton("Load File", self)
        self.load_button.clicked.connect(self.loadFile)
        vbox.addWidget(self.load_button)
        self.status_label = QLabel("Ready")
        self.statusBar().addWidget(self.status_label)
        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

    def loadFile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Archivos de Texto (*.txt);;Todos los Archivos (*)")
        if file_name:
            self.presenter.file_manager.input_file_path = file_name
            self.presenter.file_manager.storage_numbers()
            self.presenter.add_numbers()
            self.status_label.setText(f"File Selected: {file_name}")
            print(self.presenter.ri_numbers)
        
    #poker test events
    def doPokerTest(self):
        if (len(self.presenter.ri_numbers) != 0):
            pokertest = PokerTest(self.presenter.ri_numbers)
            self.presenter.poker_test = pokertest
            self.presenter.do_poker_test()
            if self.presenter.poker_test.passed:
                self.poker_tab.status.setText("Estado de la prueba: Passed")
            else:
                self.poker_tab.status.setText("Estado de la prueba: Failed")
            self.poker_tab.sum_val.setText(f"Valor de la sumatoria: {self.presenter.poker_test.total_sum}")
            self.poker_tab.chi_val.setText(f"Valor de la prueba chi inversa: {self.presenter.poker_test.chi_reverse}")

    def showGraph1Poker(self):
        self.presenter.poker_test.plot_totalSum_vs_chiReverse()
        
    def showGraph2Poker(self):
        self.presenter.poker_test.plot_oi_vs_ei()
    
    #means test events
    def doAverageTest(self):
        if (len(self.presenter.ri_numbers) != 0):
            test = AverageTest(self.presenter.ri_numbers)
            self.presenter.average_test = test
            self.presenter.do_average_test()
            if self.presenter.average_test.passed:
                self.means_tab.status.setText("Estado de la prueba: Passed")
            else:
                self.means_tab.status.setText("Estado de la prueba: Failed")
            self.means_tab.ls.setText(f"Valor Limite Superior: {self.presenter.average_test.superior_limit}")
            self.means_tab.mean.setText(f"Valor Media: {self.presenter.average_test.average}")
            self.means_tab.li.setText(f"Valor Limite Inferior: {self.presenter.average_test.inferior_limit}")
        
    def showAverageTestG(self):
        self.presenter.average_test.plotLimitsAndAverage()
        
    #variance test events
    def doVarianceTest(self):
        if (len(self.presenter.ri_numbers) != 0):
            self.presenter.variance_test = VarianceTest(self.presenter.ri_numbers)
            self.presenter.do_variance_test()
            print(self.presenter.variance_test.ri_numbers)
            if self.presenter.variance_test.passed:
                self.variance_tab.status.setText("Estado de la prueba: Passed")
            else:
                self.variance_tab.status.setText("Estado de la prueba: Failed")
            self.variance_tab.ls.setText(f"Valor Limite Superior: {self.presenter.variance_test.superior_limit}")
            self.variance_tab.variance.setText(f"Valor Varianza: {self.presenter.variance_test.variance}")
            self.variance_tab.li.setText(f"Valor Limite Inferior: {self.presenter.variance_test.inferior_limit}")
    
    def showVarianceTestG(self):
        self.presenter.variance_test.plotLimitsAndVariance()

#poker tab Class
class PokerTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # Reference to the MainWindow
        self.initUI()

    def initUI(self):
        label = QLabel("PRUEBA DE POKER\n\nDescripcion de las manos:\n (D) Todos Diferentes\n (O) Un par \n (T) Dos pares \n (K) Tercia \n (F) Tercia y Par (Full house) \n (P )Cuatro del mismo valor (poker)\n (Q) Quintilla") 
        
        self.status = QLabel("Estado de la prueba:")
        self.sum_val = QLabel("Valor de la sumatoria: ")
        self.chi_val = QLabel("Valor de la prueba chi inversa: ")
        # Create two buttons
        self.test = QPushButton("Hacer Prueba")
        self.g1 = QPushButton("Ver Gráfica Sumatoria vs Chi Inversa")
        self.g2 = QPushButton("Ver Gráfica Frecuencia de manos")
        
        self.test.clicked.connect(self.main_window.doPokerTest)
        self.g1.clicked.connect(self.main_window.showGraph1Poker)
        self.g2.clicked.connect(self.main_window.showGraph2Poker)
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.sum_val)
        layout.addWidget(self.chi_val)
        layout.addWidget(self.status)
        layout.addWidget(self.test)
        layout.addWidget(self.g1)
        layout.addWidget(self.g2)
        self.setLayout(layout)

#means tab Class
class MeansTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # Reference to the MainWindow
        self.initUI()

    def initUI(self):
        label = QLabel("PRUEBA DE MEDIAS") 
        
        self.status = QLabel("Estado de la prueba: ")
        self.ls = QLabel("Valor Limite Superior:")
        self.mean = QLabel("Valor Media:")
        self.li = QLabel("Valor Limite Inferior: ")
        # Create two buttons
        self.test = QPushButton("Hacer Prueba")
        self.g = QPushButton("Ver Limites y media")
        
        self.test.clicked.connect(self.main_window.doAverageTest)
        self.g.clicked.connect(self.main_window.showAverageTestG)
        
        layout = QVBoxLayout()
        layout.addWidget(label) #prueba de medias
        layout.addWidget(self.status)
        layout.addWidget(self.ls)
        layout.addWidget(self.mean)
        layout.addWidget(self.li)
        layout.addWidget(self.test)
        layout.addWidget(self.g)
        self.setLayout(layout)

#variance tab Class
class VarianceTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # Reference to the MainWindow
        self.initUI()

    def initUI(self):
        label = QLabel("PRUEBA DE VARIANZAS") 
        
        self.status = QLabel("Estado de la prueba: ")
        self.ls = QLabel("Valor Limite Superior:")
        self.variance = QLabel("Valor Varianza:")
        self.li = QLabel("Valor Limite Inferior: ")
        # Create two buttons
        self.test = QPushButton("Hacer Prueba")
        self.g = QPushButton("Ver Limites y Varianza")
        
        self.test.clicked.connect(self.main_window.doVarianceTest)
        self.g.clicked.connect(self.main_window.showVarianceTestG)
        
        layout = QVBoxLayout()
        layout.addWidget(label) #prueba de medias
        layout.addWidget(self.status)
        layout.addWidget(self.ls)
        layout.addWidget(self.variance)
        layout.addWidget(self.li)
        layout.addWidget(self.test)
        layout.addWidget(self.g)
        self.setLayout(layout)
        
    
    
#variance tab Class
class ChiTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        intervals = QLabel("Intervalos:")
        intervalsName = QLineEdit()
        
        layout = QVBoxLayout()
        layout.addWidget(intervals)
        layout.addWidget(intervalsName)
        self.setLayout(layout)
        
class KsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("Kolmogorov-Smirnov test")
        
        intervals = QLabel("Intervalos:")
        intervalsName = QLineEdit()
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(intervals)
        layout.addWidget(intervalsName)
        self.setLayout(layout)
