from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtGui import QFont

class ChiTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        label = QLabel("PRUEBA CHI-CUADRADO")
        font = QFont()
        font.setBold(True)
        self.status = QLabel("Estado de la prueba:")
        self.ni_min = QLabel("Valor Ni Maximo:")
        self.ni_max = QLabel("Valor Ni Minimo: ")
        self.test = QPushButton("Hacer Prueba")
        self.n = QLabel("Numero de intervalos:")
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
        
        self.intervals = QLabel("Insertar Intervalos por defecto 8:")
        self.intervalsNum = QLineEdit()
        self.intervalsNum.setValidator(double_validator)
        self.sum_chi2 = QLabel("Valor de la sumatoria de Chi2: ")
        self.chi_test = QLabel("Valor de la prueba Chi2 inversa: ")
        label.setFont(font)
        self.status.setFont(font)
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
        layout.addWidget(self.sum_chi2)
        layout.addWidget(self.chi_test)
        layout.addWidget(self.test)
        layout.addWidget(self.g)
        layout.addWidget(self.g2)
        self.setLayout(layout)    