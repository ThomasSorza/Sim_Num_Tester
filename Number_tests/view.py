import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self, Presenter):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Number test")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QTabWidget(self)
        self.setCentralWidget(self.central_widget)

        self.tab1 = TabWidget("Variance test", self)
        self.tab2 = TabWidget("KS test", self)
        self.tab3 = TabWidget("Chi2 test", self)
        self.tab4 = TabWidget("Average test", self)
        self.tab5 = TabWidget("Poker test", self)

        self.central_widget.addTab(self.tab1, "Variance test")
        self.central_widget.addTab(self.tab2, "KS test")
        self.central_widget.addTab(self.tab3, "Chi2 test")
        self.central_widget.addTab(self.tab4, "Average test")
        self.central_widget.addTab(self.tab5, "Poker test")

        self.load_button = QPushButton("Cargar Archivo", self)
        self.load_button.clicked.connect(self.loadFile)
        self.statusBar().addWidget(self.load_button)
        

    def loadFile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo", "", "Archivos de Texto (*.txt);;Todos los Archivos (*)")
        if file_name:
            print(f"Archivo seleccionado: {file_name}")


class TabWidget(QWidget):
    def __init__(self, model_name, parent):
        super().__init__(parent)
        self.model_name = model_name
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.addWidget(QPushButton(f"Conectar a {self.model_name}"))

        # Crear una gráfica de ejemplo en cada pestaña
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Generar datos de ejemplo y trazarlos
        self.plot_example_data()

        self.setLayout(layout)

    def plot_example_data(self):
        # Generar datos de ejemplo
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Crear un subplot y trazar los datos
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_title(f"Ejemplo de gráfica en {self.model_name}")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.grid(True)

        # Actualizar la gráfica
        self.canvas.draw()