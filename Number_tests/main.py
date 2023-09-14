import sys
from PyQt6.QtWidgets import QApplication
from view import MainWindow
from presenter import Presenter

def main():
    app = QApplication(sys.argv)
    presenter = Presenter()
    main_window = MainWindow(presenter)
    presenter.set_main_window(main_window)  # Establece la referencia a la ventana principal en el presentador
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
