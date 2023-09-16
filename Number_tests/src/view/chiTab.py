from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt6.QtGui import QDoubleValidator, QFont

class ChiTab(QWidget):
    """
    Clase para la pestaña de la prueba de chi-cuadrado.

    Esta clase crea la interfaz de usuario y los elementos relacionados con la prueba de chi-cuadrado.

    Args:
        main_window (MainWindow): Referencia a la ventana principal de la aplicación.

    Methods:
        initUI(): Inicializa la interfaz de usuario y los elementos relacionados con la prueba de chi-cuadrado.
    """

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.initUI()

    def initUI(self):
        """
        Inicializa la interfaz de usuario y los elementos relacionados con la prueba de chi-cuadrado.
        """
        label = QLabel("PRUEBA CHI-CUADRADO")

        # Crear una fuente en negrita para el título
        font = QFont()
        font.setBold(True)
        label.setFont(font)

        self.status = QLabel("Estado de la prueba:")
        # Crear una fuente en negrita para el estado
        font_status = QFont()
        font_status.setBold(True)
        self.status.setFont(font_status)

        self.ni_min = QLabel("Valor Ni Maximo:")
        self.ni_max = QLabel("Valor Ni Minimo: ")
        self.test = QPushButton("Hacer Prueba")
        self.n = QLabel("Numero de intervalos:")
        self.g = QPushButton("Ver Grafica Suma Chi2 y Chi2Inversa calculada")
        self.g2 = QPushButton("Ver Grafica frecuencia de los intervalos")
        self.test.clicked.connect(self.main_window.doChi2Test)
        self.g.clicked.connect(self.main_window.showChi2TestG)
        self.g2.clicked.connect(self.main_window.showChi2TestG2)
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
