import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QPushButton, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pestañas con PyQt6")
        self.setGeometry(100, 100, 400, 300)

        # Crear un widget central y un layout vertical para él
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Crear el widget de pestañas
        tab_widget = QTabWidget()

        # Crear las pestañas
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()

        # Agregar contenido a la primera pestaña (tab1)
        label1 = QLabel("Esto es el contenido de la pestaña 1")
        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.addWidget(label1)

        # Agregar contenido a la segunda pestaña (tab2)
        button2 = QPushButton("Presiona en la pestaña 2")
        tab2_layout = QVBoxLayout(tab2)
        tab2_layout.addWidget(button2)

        # Agregar contenido a la tercera pestaña (tab3)
        label3 = QLabel("Contenido de la pestaña 3")
        tab3_layout = QVBoxLayout(tab3)
        tab3_layout.addWidget(label3)

        # Agregar las pestañas al widget de pestañas
        tab_widget.addTab(tab1, "Pestaña 1")
        tab_widget.addTab(tab2, "Pestaña 2")
        tab_widget.addTab(tab3, "Pestaña 3")

        # Agregar el widget de pestañas al layout principal
        layout.addWidget(tab_widget)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
