import os.path

from ui.Texture_renamer_ui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QHeaderView, QTableWidgetItem, QComboBox, \
    QMessageBox
from PySide2.QtCore import Qt
from util.Directory import *


class Texture_renamer(QMainWindow):
    def __init__(self):
        super(Texture_renamer, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_settings()

        self.texture_dir = self.ui.T_path.text()
        self.num_of_tex = 0

        self.ui.B_finder.clicked.connect(self.open_finder)

        self.ui.B_go.clicked.connect(self.go)

    def ui_settings(self):
        self.ui.Table.setColumnWidth(0, 450)
        self.ui.Table.setColumnWidth(1, 200)
        self.ui.Table.setColumnWidth(2, 50)
        self.ui.Table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)

    def create_cbx_tex_type(self):
        ref_type = ("Basecolor",
                    "Albedo",
                    "Specular",
                    "Gloss",
                    "Roughness",
                    "Normal",
                    "Bump",
                    "Opacity",
                    "Translucency",
                    "Displacement",
                    )
        self.cbx_tex_type = QComboBox()
        self.cbx_tex_type.setFocusPolicy(Qt.StrongFocus)
        self.cbx_tex_type.addItems(ref_type)
        return self.cbx_tex_type

    def create_cbx_tex_res(self):
        ref_res = ("1K",
                   "2K",
                   "4K",
                   "8K",
                   "16K")
        self.cbx_tex_res = QComboBox()
        self.cbx_tex_type.setFocusPolicy(Qt.StrongFocus)
        self.cbx_tex_res.addItems(ref_res)
        return self.cbx_tex_res

    def open_finder(self):
        dir = QFileDialog().getExistingDirectory(None, "Select Path", "/mnt/Ripple_CG_Projects")
        if dir != "":
            self.ui.T_path.setText(dir)
            self.texture_dir = dir
            if self.texture_dir != "":
                self.num_of_tex = len(get_directory_files(self.texture_dir)[1])
                self.ui.T_name.clear()
                self.clear_table()
                self.generate_table(self.num_of_tex)
                self.fill_table()

    def generate_table(self, row_num):
        for row in range(row_num):
            self.ui.Table.insertRow(row)

    def clear_table(self):
        self.ui.Table.setRowCount(0)
        self.ui.Table.clearContents()

    def fill_table(self):
        row = 0
        files = get_directory_files(self.texture_dir)
        for file in files[1]:
            tex_name = QTableWidgetItem()
            tex_name.setText(file)
            self.ui.Table.setItem(row, 0, tex_name)
            self.ui.Table.setCellWidget(row, 1, self.create_cbx_tex_type())
            self.cbx_tex_type.setCurrentText(get_texture_type(file))
            self.ui.Table.setCellWidget(row, 2, self.create_cbx_tex_res())
            self.cbx_tex_res.setCurrentText(get_tex_res(file))
            row += 1

    def go(self):
        if self.num_of_tex != 0:
            if self.ui.T_name.text() != "":
                for row in range(0, self.num_of_tex):
                    tex_name = self.ui.Table.item(row, 0).text()
                    old_tex_path = os.path.join(self.texture_dir, tex_name)
                    tex_type = self.ui.Table.cellWidget(row, 1).currentText()
                    tex_res = self.ui.Table.cellWidget(row, 2).currentText()
                    new_tex_name = self.ui.T_name.text() + "_" + tex_type + "_" + tex_res + "." + tex_name.split(".")[
                        -1]
                    new_tex_path = os.path.join(self.texture_dir, new_tex_name)
                    rename(old_tex_path, new_tex_path)

                    item_tex_name = QTableWidgetItem()
                    item_tex_name.setText(new_tex_name)
                    self.ui.Table.setItem(row, 0, item_tex_name)
                self.ui.statusbar.showMessage("Successfully renamed ◔̯◔")
            else:
                QMessageBox.warning(None, "Warning", "Asset Name is Empty!")


if __name__ == '__main__':
    import sys

    app = QApplication([])
    window = Texture_renamer()
    window.show()
    sys.exit(app.exec_())
