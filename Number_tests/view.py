import sys
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from presenter import Presenter

class MainWindow(QMainWindow):
    def __init__(self, presenter):
        super().__init__()
        self.initUI()
        self.presenter = presenter

    def initUI(self):
        self.setWindowTitle("Number tests")
        tab_widget = QTabWidget()
        tab_widget.addTab(PokerTab(), "Poker Test")
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


class PokerTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("Poker Test")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
class ChiTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("Chi2 Test")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
class MeansTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("Means Test")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
class VarianceTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("Variance Test")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
class KsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("Kolmogorov-Smirnov test")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
