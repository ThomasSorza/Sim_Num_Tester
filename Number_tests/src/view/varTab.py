from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QDoubleValidator, QFont

# Variance tab Class
class VarianceTab(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # Reference to the MainWindow
        self.initUI()

    def initUI(self):
        label_text = "PRUEBA DE VARIANZAS"
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

        self.ls = QLabel("Valor Limite Superior:")
        self.variance = QLabel("Valor Varianza:")
        self.li = QLabel("Valor Limite Inferior: ")
        self.test = QPushButton("Hacer Prueba")
        self.g = QPushButton("Ver Limites y Varianza")
        self.test.clicked.connect(self.main_window.doVarianceTest)
        self.g.clicked.connect(self.main_window.showVarianceTestG)
        layout = QVBoxLayout()
        layout.addWidget(label)  # prueba de varianzas
        layout.addWidget(self.status)
        layout.addWidget(self.ls)
        layout.addWidget(self.variance)
        layout.addWidget(self.li)
        layout.addWidget(self.test)
        layout.addWidget(self.g)
        self.setLayout(layout)
