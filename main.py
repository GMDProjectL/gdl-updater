from PySide6.QtWidgets import QApplication
from main_window import MainWindow


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow('/opt/installer')

    window.setModal(True)
    window.show()

    window.run_download()
    
    exit(app.exec())