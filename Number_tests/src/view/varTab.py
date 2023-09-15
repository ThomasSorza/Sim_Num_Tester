from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QDoubleValidator


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