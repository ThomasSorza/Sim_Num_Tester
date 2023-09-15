import sys
from PyQt6.QtWidgets import QApplication
from view.view import MainWindow
from controller.presenter import Presenter

def main():
    """
    Función principal de la aplicación.
    """
    # Crear una instancia de la aplicación PyQt6
    app = QApplication(sys.argv)
    
    # Crear una instancia del presentador de la aplicación
    presenter = Presenter()
    
    # Crear una instancia de la ventana principal de la aplicación
    main_window = MainWindow(presenter)
    
    # Establecer la referencia a la ventana principal en el presentador
    presenter.set_main_window(main_window)
    
    # Mostrar la ventana principal
    main_window.show()
    
    # Iniciar el bucle de eventos de la aplicación
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
