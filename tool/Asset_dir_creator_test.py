from util.Directory import *
from PySide2.QtWidgets import QApplication, QFileDialog, QMainWindow
from ui.asset_creator_ui import Ui_MainWindow


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
        if self.ui.CB_mdl.isChecked():
            dir_struct = (
                "Geo",
                "Geo/Variant",
                "Geo/Variant/Abc"
            )
            create_dir(self.asset_name, self.asset_path, dir_struct)
        if self.ui.CB_ldv.isChecked():
            dir_struct = (
                "Looks",
                "Looks/Texture",
                "Looks/Texture/Preview",
                "Looks/Texture/Render"
            )
            create_dir(self.asset_name, self.asset_path, dir_struct)
        if self.ui.CB_rig.isChecked():
            dir_struct = (
                "Rig",
            )
            create_dir(self.asset_name, self.asset_path, dir_struct)
        if self.ui.CB_anim.isChecked():
            dir_struct = (
                "Anim",
            )
            create_dir(self.asset_name, self.asset_path, dir_struct)
        self.ui.statusbar.showMessage("Successfully created asset directory ◔̯◔")


if __name__ == "__main__":
    import sys

    app = QApplication([])
    window = Asset_dir_creator()
    window.show()
    sys.exit(app.exec_())
