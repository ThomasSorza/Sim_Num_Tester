import sys
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QLineEdit, QVBoxLayout, QLabel, QPushButton, QFileDialog
from presenter import Presenter
from poker_test import PokerTest
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
        tab_widget.addTab(self.poker_tab, "Poker Test")
        tab_widget.addTab(MeansTab(), "Means Test")
        tab_widget.addTab(VarianceTab(), "Variance Test")
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
            
    def doPokerTest(self):
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

class PokerTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # Reference to the MainWindow
        self.initUI()

    def initUI(self):
        label = QLabel("Descripcion de las manos:\n (D) Todos Diferentes\n (O) Un par \n (T) Dos pares \n (K) Tercia \n (F) Tercia y Par (Full house) \n (P )Cuatro del mismo valor (poker)\n (Q) Quintilla") 
        
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
        
class MeansTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("PRUEBA DE MEDIAS") 
        
        self.status = QLabel("Estado de la prueba: ")
        self.ls = QLabel("Valor Limite Superior:")
        self.mean = QLabel("Valor Media:")
        self.li = QLabel("Valor Limite Inferior: ")
        # Create two buttons
        self.test = QPushButton("Hacer Prueba")
        self.grafica = QPushButton("Ver Limites y media")
        
        self.test.clicked.connect(self.doTest)
        self.grafica.clicked.connect(self.showGraph)
        
        layout = QVBoxLayout()
        layout.addWidget(label) #prueba de medias
        layout.addWidget(self.status)
        layout.addWidget(self.ls)
        layout.addWidget(self.mean)
        layout.addWidget(self.li)
        layout.addWidget(self.test)
        layout.addWidget(self.grafica)
        self.setLayout(layout)
        
    def doTest(self):
        #super.exe_test()
        test = True
        if test:
            self.status.setText("Estado de la prueba: Passed")
        else:
            self.status.setText("Estado de la prueba: Failed")
        # Define the function to be executed when button0 is clicked
        print("Hacer Prueba button clicked")
    
    def showGraph(self):
        #plot
        print("grafica")
        
class VarianceTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("PRUEBA DE VARIANZAS") 
        
        self.status = QLabel("Estado de la prueba: ")
        self.ls = QLabel("Valor Limite Superior:")
        self.mean = QLabel("Valor Varianza:")
        self.li = QLabel("Valor Limite Inferior: ")
        # Create two buttons
        self.test = QPushButton("Hacer Prueba")
        self.grafica = QPushButton("Ver Limites y Varianza")
        
        self.test.clicked.connect(self.doTest)
        self.grafica.clicked.connect(self.showGraph)
        
        layout = QVBoxLayout()
        layout.addWidget(label) #prueba de medias
        layout.addWidget(self.status)
        layout.addWidget(self.ls)
        layout.addWidget(self.mean)
        layout.addWidget(self.li)
        layout.addWidget(self.test)
        layout.addWidget(self.grafica)
        self.setLayout(layout)
        
    def doTest(self):
        #super.exe_test()
        test = True
        if test:
            self.status.setText("Estado de la prueba: Passed")
        else:
            self.status.setText("Estado de la prueba: Failed")
        # Define the function to be executed when button0 is clicked
        print("Hacer Prueba button clicked")
    
    def showGraph(self):
        #plot
        print("grafica")
        
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
