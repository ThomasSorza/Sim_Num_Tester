from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QDoubleValidator, QFont

class KsTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        label = QLabel("PRUEBA Kolmogorov-Smirnov")
        
        # Crear una fuente en negrita
        font = QFont()
        font.setBold(True)
        label.setFont(font)

        self.status = QLabel("Estado de la prueba:")
        
        # Crear una fuente en negrita
        font_status = QFont()
        font_status.setBold(True)
        self.status.setFont(font_status)

        self.mean = QLabel("Promedio de los datos:")
        self.d_max = QLabel("Valor del D_max:")
        self.d_max_p = QLabel("Valor del d_max_p: ")
        self.test = QPushButton("Hacer Prueba")
        self.n = QLabel("Numero de intervalos Por defecto 8:")
        self.g = QPushButton("Ver Grafica d_max y d_max_p")
        self.g2 = QPushButton("Ver Grafica de probabilidad de todos los Intervalos")
        self.g3 = QPushButton("Ver Grafica frecuencia de los intervalos")
        self.test.clicked.connect(self.main_window.doKsTest)
        self.g.clicked.connect(self.main_window.showKsTestG)
        self.g2.clicked.connect(self.main_window.showKsTestG2)
        self.g3.clicked.connect(self.main_window.showKsTestG3)
        self.intervals = QLabel("Insertar Intervalos por defecto 10:")
        self.intervalsNum = QLineEdit()
        double_validator = QDoubleValidator()
        self.intervalsNum.setValidator(double_validator)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.intervals)
        layout.addWidget(self.intervalsNum)
        layout.addWidget(self.status)
        layout.addWidget(self.mean)
        layout.addWidget(self.d_max)
        layout.addWidget(self.d_max_p)
        layout.addWidget(self.test)
        layout.addWidget(self.g3)
        layout.addWidget(self.g)
        layout.addWidget(self.g2)
        self.setLayout(layout)
