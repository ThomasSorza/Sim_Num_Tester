import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QDialogButtonBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Number tests")
        tab_widget = QTabWidget()
        tab_widget.addTab(PokerTab(), "Poker Test")
        tab_widget.addTab(MeansTab(), "Means Test")
        tab_widget.addTab(VarianceTab(), "Variance Test")
        tab_widget.addTab(KsTab(), "K-S Test")
        tab_widget.addTab(ChiTab(), "Chi2 Test")  # Corrección aquí
        
        
        
        vbox = QVBoxLayout()
        vbox.addWidget(tab_widget)
        
        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

class PokerTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Aquí puedes agregar elementos a la pestaña de Poker Test
        label = QLabel("Poker Test")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
class ChiTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Aquí puedes agregar elementos a la pestaña de Poker Test
        label = QLabel("Chi2 Test")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
class MeansTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Aquí puedes agregar elementos a la pestaña de Poker Test
        label = QLabel("Means Test")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
class VarianceTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Aquí puedes agregar elementos a la pestaña de Poker Test
        label = QLabel("Variance Test")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
class KsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Aquí puedes agregar elementos a la pestaña de Poker Test
        label = QLabel("Kolmogorov-Smirnov test")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
