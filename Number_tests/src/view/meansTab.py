from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont

class MeansTab(QWidget):
    """
    Clase para la pestaña de la prueba de medias.

    Esta clase crea la interfaz de usuario y los elementos relacionados con la prueba de medias.

    Args:
        main_window (MainWindow): Referencia a la ventana principal de la aplicación.

    Methods:
        initUI(): Inicializa la interfaz de usuario y los elementos relacionados con la prueba de medias.
    """

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # Referencia a la ventana MainWindow
        self.initUI()

    def initUI(self):
        """
        Inicializa la interfaz de usuario y los elementos relacionados con la prueba de medias.
        """
        label_text = "PRUEBA DE MEDIAS"
        label = QLabel(label_text)

        # Crear una fuente en negrita para el título
        font = QFont()
        font.setBold(True)
        label.setFont(font)

        self.status = QLabel("Estado de la prueba:")
        # Crear una fuente en negrita para el estado
        font_status = QFont()
        font_status.setBold(True)
        self.status.setFont(font_status)

        self.ls = QLabel("Valor Limite Superior:")
        self.mean = QLabel("Valor Media:")
        self.li = QLabel("Valor Limite Inferior: ")
        self.test = QPushButton("Hacer Prueba")
        self.g = QPushButton("Ver Limites y Media")
        self.test.clicked.connect(self.main_window.doAverageTest)
        self.g.clicked.connect(self.main_window.showAverageTestG)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.status)
        layout.addWidget(self.ls)
        layout.addWidget(self.mean)
        layout.addWidget(self.li)
        layout.addWidget(self.test)
        layout.addWidget(self.g)
        self.setLayout(layout)
