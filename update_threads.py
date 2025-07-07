from PySide6 import QtCore
from update import download_and_unpack_installer, install_dependencies, build_installer
from traceback import format_exc


class UpdateStepThread(QtCore.QThread):
    finished_signal = QtCore.Signal(bool, str) # Is successful
    installer_dir = ''

    def __init__(self, parent = None, installer_dir = '/opt/installer'):
        super().__init__(parent)
        self.installer_dir = installer_dir


class DownloadingThread(UpdateStepThread):
    def run(self):
        try:
            download_and_unpack_installer(self.installer_dir)
            self.finished_signal.emit(True, "")
        except Exception:
            self.finished_signal.emit(False, format_exc())


class InstallingDependenciesThread(UpdateStepThread):
    def run(self):
        try:
            result = install_dependencies(self.installer_dir)
            if result != 0:
                self.finished_signal.emit(False, f"Failed to install dependencies. Code: {result}")
                return
            self.finished_signal.emit(True, "")
        except Exception:
            self.finished_signal.emit(False, format_exc())


class BuildingThread(UpdateStepThread):
    def run(self):
        try:
            result = build_installer(self.installer_dir)
            if result != 0:
                self.finished_signal.emit(False, f"Failed to build the installer. Code: {result}")
                return
            self.finished_signal.emit(True, "")
        except Exception:
            self.finished_signal.emit(False, format_exc())