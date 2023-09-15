import sys
from PyQt6.QtWidgets import QMainWindow, QTabWidget,QMessageBox, QWidget, QLineEdit, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt6.QtGui import QDoubleValidator

from controller.presenter import Presenter
from model.poker_test import PokerTest
from model.average_test import AverageTest
from model.variance_test import VarianceTest
from model.ks_test import KsTest
from model.chi2_test import ChiTest
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
        self.ks_tab = KsTab(self)
        self.chi_tab = ChiTab(self)
        tab_widget.addTab(self.poker_tab, "Poker Test")
        tab_widget.addTab(self.means_tab, "Means Test")
        tab_widget.addTab(self.variance_tab, "Variance Test")
        tab_widget.addTab(self.ks_tab, "K-S Test")
        tab_widget.addTab(self.chi_tab, "Chi2 Test")
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
    
    def showErrorMessage(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()
        
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
            if self.presenter.variance_test.passed:
                self.variance_tab.status.setText("Estado de la prueba: Passed")
            else:
                self.variance_tab.status.setText("Estado de la prueba: Failed")
            self.variance_tab.ls.setText(f"Valor Limite Superior: {self.presenter.variance_test.superior_limit}")
            self.variance_tab.variance.setText(f"Valor Varianza: {self.presenter.variance_test.variance}")
            self.variance_tab.li.setText(f"Valor Limite Inferior: {self.presenter.variance_test.inferior_limit}")
    
    def showVarianceTestG(self):
        self.presenter.variance_test.plotLimitsAndVariance()
    
    #ks test events
    def doKsTest(self):
        if(len(self.presenter.ri_numbers) != 0):
            if(self.ks_tab.intervalsNum.text() != ""):
                self.presenter.ks_test = KsTest(self.presenter.ri_numbers, int(self.ks_tab.intervalsNum.text()))
            else:
                self.presenter.ks_test = KsTest(self.presenter.ri_numbers)
            self.presenter.do_ks_test()
            if self.presenter.ks_test.passed:
                self.ks_tab.status.setText("Estado de la prueba: Passed")
            else:
                self.ks_tab.status.setText("Estado de la prueba: Failed")
            self.ks_tab.mean.setText(f"Promedio de los datos: {self.presenter.ks_test.average}")
            self.ks_tab.d_max.setText(f"Valor del D_max: {self.presenter.ks_test.d_max}")
            self.ks_tab.d_max_p.setText(f"Valor del d_max_p: {self.presenter.ks_test.d_max_p}")
            self.ks_tab.n.setText(f"Numero de intervalos: {self.presenter.ks_test.n_intervals}")
    
    def showKsTestG(self):
        self.presenter.ks_test.plotDs()
    
    def showKsTestG2(self):
        self.presenter.ks_test.plotIntervals()
    
    def showKsTestG3(self):
        self.presenter.ks_test.plotIntervalsFreq()
    
    #chi2 test events
    def doChi2Test(self):
        if len(self.presenter.ri_numbers) != 0:
            numIntervals = self.chi_tab.intervalsNum.text()
            a = self.chi_tab.a_input.text()
            b = self.chi_tab.b_input.text()
            if numIntervals != "" and a != "" and b != "":
                self.presenter.chi2_test = ChiTest(self.presenter.ri_numbers, int(numIntervals), float(a), float(b))
            elif numIntervals != "" and a != "" and b == "":
                self.showErrorMessage("Error", "Falta el valor de b.")
                return#do not continue with the function
            elif numIntervals != "" and a == "" and b != "":
                self.showErrorMessage("Error", "Falta el valor de a.")
                return#do not continue with the function
            else :
                self.presenter.chi2_test = ChiTest(self.presenter.ri_numbers)
            self.presenter.do_chi2_test()
            if self.presenter.chi2_test.passed:
                self.chi_tab.status.setText("Estado de la prueba: Passed")
            else:
                self.chi_tab.status.setText("Estado de la prueba: Failed")
            self.chi_tab.ni_min.setText(f"Valor Ni Maximo: {str(self.presenter.chi2_test.niMax)}")
            self.chi_tab.ni_max.setText(f"Valor Ni Minimo: {str(self.presenter.chi2_test.niMin)}")
            self.chi_tab.n.setText(f"Numero de intervalos: {self.presenter.chi2_test.intervals_amount}")

    
    def showChi2TestG(self):
        self.presenter.chi2_test.plotChi2()
        
    def showChi2TestG2(self):
        self.presenter.chi2_test.plotFrequencies()
        
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
        
#Ks tab Class
class KsTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        label = QLabel("PRUEBA Kolmogorov-Smirnov")
        self.status = QLabel("Estado de la prueba: ")
        self.mean = QLabel("Promedio de los datos:")
        self.d_max = QLabel("Valor del D_max:")
        self.d_max_p = QLabel("Valor del d_max_p: ")
        self.test = QPushButton("Hacer Prueba")
        self.n = QLabel("Numero de intervalos:")
        self.g = QPushButton("Ver Grafica d_max y d_max_p")
        self.g2 = QPushButton("Ver Grafica de probabilidad de todos los Intervalos")
        self.g3 = QPushButton("Ver Grafica frecuencia de los intervalos")
        self.test.clicked.connect(self.main_window.doKsTest)
        self.g.clicked.connect(self.main_window.showKsTestG)
        self.g2.clicked.connect(self.main_window.showKsTestG2)
        self.g3.clicked.connect(self.main_window.showKsTestG3)
        self.intervals = QLabel("Insertar Intervalos:")
        self.intervalsNum = QLineEdit()
        double_validator = QDoubleValidator()
        self.intervalsNum.setValidator(double_validator)
        self.a = QLabel("Insertar valor de a para Ni (menor):")
        self.aNum = QLineEdit()
        self.aNum.setValidator(double_validator)
        layout = QVBoxLayout()
        self.b = QLabel("Insertar valor de b para Ni (mayor):")
        self.bNum = QLineEdit()
        self.bNum.setValidator(double_validator)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.intervals)
        layout.addWidget(self.intervalsNum)
        layout.addWidget(self.a)
        layout.addWidget(self.aNum)
        layout.addWidget(self.b)
        layout.addWidget(self.bNum)
        layout.addWidget(self.n)
        layout.addWidget(self.status)
        layout.addWidget(self.mean)
        layout.addWidget(self.d_max)
        layout.addWidget(self.d_max_p)
        layout.addWidget(self.test)
        layout.addWidget(self.g3)
        layout.addWidget(self.g)
        layout.addWidget(self.g2)
        self.setLayout(layout)

#Chi2 tab Class
class ChiTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        label = QLabel("PRUEBA CHI-CUADRADO")
        self.status = QLabel("Estado de la prueba: ")
        self.ni_min = QLabel("Valor Ni Maximo:")
        self.ni_max = QLabel("Valor Ni Minimo: ")
        self.test = QPushButton("Hacer Prueba")
        self.n = QLabel("Numero de intervalos por defecto 8:")
        self.g = QPushButton("Ver Grafica Suma Chi2 y Chi2Inversa calculada")
        self.g2 = QPushButton("Ver Grafica frecuencia de los intervalos")
        self.test.clicked.connect(self.main_window.doChi2Test)
        self.g.clicked.connect(self.main_window.showChi2TestG)
        self.g2.clicked.connect(self.main_window.showChi2TestG2)
        # Input fields for 'a' and 'b'
        self.a_label = QLabel("Valor 'a' (Valor mas bajo Ni) por defecto 8:")
        self.b_label = QLabel("Valor 'b' (Valor mas alto Ni) por defecto 10:")
        self.a_input = QLineEdit()
        self.b_input = QLineEdit()
        double_validator = QDoubleValidator()
        self.a_input.setValidator(double_validator)
        self.b_input.setValidator(double_validator)
        
        self.intervals = QLabel("Insertar Intervalos:")
        self.intervalsNum = QLineEdit()
        self.intervalsNum.setValidator(double_validator)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.intervals)
        layout.addWidget(self.intervalsNum)
        layout.addWidget(self.a_label)
        layout.addWidget(self.a_input)
        layout.addWidget(self.b_label)
        layout.addWidget(self.b_input)
        layout.addWidget(self.n)
        layout.addWidget(self.status)
        layout.addWidget(self.ni_max)
        layout.addWidget(self.ni_min)
        layout.addWidget(self.test)
        layout.addWidget(self.g)
        layout.addWidget(self.g2)
        self.setLayout(layout)    