from util.Directory import *
from PySide2.QtWidgets import QApplication, QFileDialog, QMainWindow
from ui.asset_tool_ui import Ui_MainWindow


class Asset_dir_creator(QMainWindow):

    def __init__(self):
        super(Asset_dir_creator, self).__init__()

        self.asset_name = ""
        self.asset_path = ""

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.B_finder.clicked.connect(self.open_finder)
        self.ui.B_go.clicked.connect(self.go)

    def set_asset_name(self):
        self.asset_name = self.ui.T_name.text()

    def set_asset_path(self):
        self.ui.T_path.setText(self.asset_path)

    def open_finder(self):
        self.asset_path = QFileDialog().getExistingDirectory(None, "Select Path", "/mnt/Ripple_CG_Projects")
        if self.asset_path != "":
            self.set_asset_name()
            self.set_asset_path()

    def go(self):
        self.set_asset_name()
        create_dir(self.asset_name, self.asset_path)


if __name__ == "__main__":
    import sys

    app = QApplication([])
    window = Asset_dir_creator()
    window.show()
    sys.exit(app.exec_())
