import sys, os, subprocess

# Prompt user to install missing packages upon import error
packages = ["sqlite3", "PySide6", "shutil"]

for package in packages:
    try:
        __import__(package)
    except ImportError:
        # Ask user if they want to install (in console)
        response = input(
            f"The package '{package}' needed to run this utility is not installed. Do you want to install it now? (y/n): "
        )
        if response.lower() == "y":
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            #__import__(package)  # Try importing again after installation


import sqlite3
import shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableView, QComboBox, QVBoxLayout, QPushButton, QWidget
from PySide6.QtCore import QAbstractTableModel, Qt

class SQLiteTableModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super().__init__()
        self._data = data
        self._headers = headers

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0]) if self._data else 0

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._headers[section]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SQLite File Copier')
        self.setGeometry(300, 300, 800, 600)

        layout = QVBoxLayout()

        self.comboBox = QComboBox()
        self.comboBox.currentIndexChanged.connect(self.load_data)
        layout.addWidget(self.comboBox)

        self.tableView = QTableView()
        layout.addWidget(self.tableView)

        self.processButton = QPushButton("Process Files")
        self.processButton.clicked.connect(self.process_files)
        layout.addWidget(self.processButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.app_dir = ""

        self.open_database()

    def open_database(self):
        options = QFileDialog.Options()
        db_path, _ = QFileDialog.getOpenFileName(self, "Open SQLite Database", "", "SQLite Manifest (*.db);;All Files (*)", options=options)
        if db_path:
            self.app_dir = os.path.dirname(db_path)
            self.connection = sqlite3.connect(db_path)
            self.comboBox.addItem("Files")

    def load_data(self):
        query = "SELECT fileID, relativePath, file FROM Files WHERE domain = 'CameraRollDomain' AND relativePath LIKE 'Media/DCIM/101APPLE/%'"
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        # Find the full paths of the files
        updated_result = []
        for row in result:
            fileID = row[0]
            relativePath = row[1]
            file_blob = row[2]
            full_path = self.find_file(self.app_dir, fileID)
            full_path = full_path.replace("\\", "/")  # Convert backslashes to forward slashes
            updated_result.append((fileID, relativePath, file_blob, full_path))

        headers = ["FileID", "RelativePath", "FileBlob", "FullPath"]
        self.model = SQLiteTableModel(updated_result, headers)
        self.tableView.setModel(self.model)

    def find_file(self, directory, filename):
        for root, _, files in os.walk(directory):
            if filename in files:
                return os.path.join(root, filename)
        return ""

    def process_files(self):
        query = "SELECT fileID, relativePath FROM Files WHERE domain = 'CameraRollDomain' AND relativePath LIKE 'Media/DCIM/101APPLE/%'"
        cursor = self.connection.cursor()
        cursor.execute(query)
        files = cursor.fetchall()

        dcim_dir = os.path.join(self.app_dir, 'DCIM')
        os.makedirs(dcim_dir, exist_ok=True)

        for fileID, relativePath in files:
            full_path = self.find_file(self.app_dir, fileID)
            if full_path:
                new_filename = relativePath.split('Media/DCIM/101APPLE/')[-1]
                new_path = os.path.join(dcim_dir, new_filename)
                if os.path.isfile(full_path):
                    os.makedirs(os.path.dirname(new_path), exist_ok=True)
                    shutil.copy(full_path, new_path)

        QMessageBox.information(self, "Success", "Files have been processed and copied to DCIM folder")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
