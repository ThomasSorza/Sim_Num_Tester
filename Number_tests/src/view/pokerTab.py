from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QDoubleValidator, QFont

#poker tab Class
class PokerTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # Reference to the MainWindow
        self.initUI()

    def initUI(self):
        label_text = "PRUEBA DE POKER\n\nDescripcion de las manos:\n (D) Todos Diferentes\n (O) Un par \n (T) Dos pares \n (K) Tercia \n (F) Tercia y Par (Full house) \n (P )Cuatro del mismo valor (poker)\n (Q) Quintilla"
        label = QLabel(label_text)

        # Crear una fuente en negrita
        font = QFont()
        font.setBold(True)
        label.setFont(font)

        self.status = QLabel("Estado de la prueba:")
        
        # Crear una fuente en negrita
        font_status = QFont()
        font_status.setBold(True)
        self.status.setFont(font_status)

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
