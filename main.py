from update import download_and_deploy_installer, run_installer_backend, run_installer_frontend, run_electron_window
from threading import Thread
from update_threads import DownloadingThread, InstallingDependenciesThread, BuildingThread
from PySide6 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QProgressDialog):
    installer_dir: str = ''

    def __init__(self, installer_dir: str = '/opt/installer'):
        super().__init__()
        self.installer_dir = installer_dir
        self.setMinimum(0)
        self.setMaximum(0)
        self.setMinimumDuration(0)
        self.setMinimumSize(300, 150)
        self.setMaximumSize(300, 150)
        self.setWindowTitle("System Updater")
        self.setCancelButton(None)
    

    def run_download(self):
        self.setLabelText("Downloading...")
        worker_thread = DownloadingThread(self, self.installer_dir)
        worker_thread.finished_signal.connect(self.downloading_done)
        worker_thread.start()
        
    @QtCore.Slot()
    def downloading_done(self, success: bool, message: str):
        if not success:
            QtWidgets.QMessageBox.warning(self, "Error", message)
            return

        self.setLabelText("Downloading done")
        self.run_installing_dependencies()
    

    def run_installing_dependencies(self):
        self.setLabelText("Installing dependencies...")
        worker_thread = InstallingDependenciesThread(self, self.installer_dir)
        worker_thread.finished_signal.connect(self.installing_dependencies_done)
        worker_thread.start()
        
    @QtCore.Slot()
    def installing_dependencies_done(self, success: bool, message: str):
        if not success:
            QtWidgets.QMessageBox.warning(self, "Error", message)
            return

        self.setLabelText("Dependencies done")
        self.run_building()
    

    def run_building(self):
        self.setLabelText("Building the installer...")
        worker_thread = BuildingThread(self, self.installer_dir)
        worker_thread.finished_signal.connect(self.building_done)
        worker_thread.start()
        
    @QtCore.Slot()
    def building_done(self, success: bool, message: str):
        if not success:
            QtWidgets.QMessageBox.warning(self, "Error", message)
            return

        self.setLabelText("Building done")
        self.run_installer()
    
    
    def run_installer(self):
        self.hide()

        backend_thread = Thread(target=run_installer_backend, args=(self.installer_dir,))
        backend_thread.start()

        frontend_thread = Thread(target=run_installer_frontend, args=(self.installer_dir,))
        frontend_thread.start()

        run_electron_window(self.installer_dir)




if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = MainWindow('/opt/installer')

    window.setModal(True)
    window.show()

    window.run_download()
    
    exit(app.exec())

#installer_dir = '/opt/installer'
#download_and_deploy_installer(installer_dir)

