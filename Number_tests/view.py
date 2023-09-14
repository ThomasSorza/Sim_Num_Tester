import sys
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QLineEdit, QVBoxLayout, QLabel, QPushButton, QFileDialog
from presenter import Presenter

class MainWindow(QMainWindow):
    def __init__(self, presenter):
        super().__init__()
        self.initUI()
        self.presenter = presenter

    def initUI(self):
        self.setWindowTitle("Number tests")
        self.setGeometry(100, 100, 500, 400) 
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
        label = QLabel("Descripcion de las manos:\n (D) Todos Diferentes\n (O) Un par \n (T) Dos pares \n (K) Tercia \n (F) Tercia y Par (Full house) \n (P )Cuatro del mismo valor (poker)\n (Q) Quintilla") 
        
        self.status = QLabel("Estado de la prueba:")
        self.sum_val = QLabel("Valor de la sumatoria: ")
        self.chi_val = QLabel("Valor de la prueba chi inversa: ")
        # Create two buttons
        self.button0 = QPushButton("Hacer Prueba")
        self.button1 = QPushButton("Ver Gráfica Dmax y Dmax_p")
        self.button2 = QPushButton("Ver Gráfica Frecuencia de manos")
        
        self.button0.clicked.connect(self.doTest)
        self.button1.clicked.connect(self.showGraph1)
        self.button2.clicked.connect(self.showGraph2)
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.sum_val)
        layout.addWidget(self.chi_val)
        layout.addWidget(self.status)
        layout.addWidget(self.button0)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)
        
    def doTest(self):
        #super.exe_test()
        test = True
        if test:
            self.status.setText("Estado de la prueba: Passed")
        else:
            self.status.setText("Estado de la prueba: Failed")
        # Define the function to be executed when button0 is clicked
        print("Hacer Prueba button clicked")

    def showGraph1(self):
        # Define the function to be executed when button1 is clicked
        print("Ver Gráfica 1 button clicked")

    def showGraph2(self):
        # Define the function to be executed when button2 is clicked
        print("Ver Gráfica 2 button clicked")
        
class ChiTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        intervals = QLabel("Intervalos:")
        intervalsName = QLineEdit()
        
        layout = QVBoxLayout()
        layout.addWidget(intervals)
        layout.addWidget(intervalsName)
        self.setLayout(layout)
        
class MeansTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("PRUEBA DE MEDIAS") 
        
        self.status = QLabel("Estado de la prueba: ")
        self.ls = QLabel("Valor Limite Superior:")
        self.mean = QLabel("Valor Media:")
        self.li = QLabel("Valor Limite Inferior: ")
        # Create two buttons
        self.test = QPushButton("Hacer Prueba")
        self.grafica = QPushButton("Ver Limites y media")
        
        self.test.clicked.connect(self.doTest)
        self.grafica.clicked.connect(self.showGraph)
        
        layout = QVBoxLayout()
        layout.addWidget(label) #prueba de medias
        layout.addWidget(self.status)
        layout.addWidget(self.ls)
        layout.addWidget(self.mean)
        layout.addWidget(self.li)
        layout.addWidget(self.test)
        layout.addWidget(self.grafica)
        self.setLayout(layout)
        
    def doTest(self):
        #super.exe_test()
        test = True
        if test:
            self.status.setText("Estado de la prueba: Passed")
        else:
            self.status.setText("Estado de la prueba: Failed")
        # Define the function to be executed when button0 is clicked
        print("Hacer Prueba button clicked")
    
    def showGraph(self):
        #plot
        print("grafica")
        
class VarianceTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("PRUEBA DE VARIANZAS") 
        
        self.status = QLabel("Estado de la prueba: ")
        self.ls = QLabel("Valor Limite Superior:")
        self.mean = QLabel("Valor Varianza:")
        self.li = QLabel("Valor Limite Inferior: ")
        # Create two buttons
        self.test = QPushButton("Hacer Prueba")
        self.grafica = QPushButton("Ver Limites y Varianza")
        
        self.test.clicked.connect(self.doTest)
        self.grafica.clicked.connect(self.showGraph)
        
        layout = QVBoxLayout()
        layout.addWidget(label) #prueba de medias
        layout.addWidget(self.status)
        layout.addWidget(self.ls)
        layout.addWidget(self.mean)
        layout.addWidget(self.li)
        layout.addWidget(self.test)
        layout.addWidget(self.grafica)
        self.setLayout(layout)
        
    def doTest(self):
        #super.exe_test()
        test = True
        if test:
            self.status.setText("Estado de la prueba: Passed")
        else:
            self.status.setText("Estado de la prueba: Failed")
        # Define the function to be executed when button0 is clicked
        print("Hacer Prueba button clicked")
    
    def showGraph(self):
        #plot
        print("grafica")
        
class KsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("Kolmogorov-Smirnov test")
        
        intervals = QLabel("Intervalos:")
        intervalsName = QLineEdit()
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(intervals)
        layout.addWidget(intervalsName)
        self.setLayout(layout)
