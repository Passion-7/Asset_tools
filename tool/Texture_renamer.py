from ui.Texture_renamer_ui import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QHeaderView, QTableWidgetItem, QComboBox, QMessageBox
from util.Directory import *


class Texture_renamer(QMainWindow):
    def __init__(self):
        super(Texture_renamer, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_settings()

        self.texture_dir = ""

        self.ui.B_finder.clicked.connect(self.open_finder)

        self.ui.B_go.clicked.connect(self.go)

    def ui_settings(self):
        self.ui.Table.setColumnWidth(0, 450)
        self.ui.Table.setColumnWidth(1, 200)
        self.ui.Table.setColumnWidth(2, 50)
        self.ui.Table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.Table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)

    def create_cbx_tex_type(self):
        self.cbx_tex_type = QComboBox()
        self.cbx_tex_type.addItem("Basecolor")
        self.cbx_tex_type.addItem("Specular")
        self.cbx_tex_type.addItem("Gloss")
        self.cbx_tex_type.addItem("Roughness")
        self.cbx_tex_type.addItem("Normal")
        self.cbx_tex_type.addItem("Bump")
        self.cbx_tex_type.addItem("Opacity")
        self.cbx_tex_type.addItem("Translucency")
        self.cbx_tex_type.addItem("Displacement")
        return self.cbx_tex_type

    def create_cbx_tex_res(self):
        ref_res = ("1K",
                   "2K",
                   "4K",
                   "8K",
                   "16K")
        self.cbx_tex_res = QComboBox()
        self.cbx_tex_res.addItems(ref_res)
        return self.cbx_tex_res

    def open_finder(self):
        self.texture_dir = QFileDialog().getExistingDirectory(None, "Select Path", "/mnt/Ripple_CG_Projects")
        if self.texture_dir != "":
            self.ui.T_path.setText(self.texture_dir)
            self.texture_file_list()

    def texture_file_list(self):
        files = get_directory_files(self.texture_dir)
        row_num = 0

        for file in files[1]:
            tex_name = QTableWidgetItem()
            tex_name.setText(file)
            self.ui.Table.insertRow(row_num)
            self.ui.Table.setItem(row_num, 0, tex_name)
            self.ui.Table.setCellWidget(row_num, 1, self.create_cbx_tex_type())
            self.cbx_tex_type.setCurrentText(get_texture_type(file))
            self.ui.Table.setCellWidget(row_num, 2, self.create_cbx_tex_res())
            self.cbx_tex_res.setCurrentText(get_tex_res(file))
            row_num += 1

    def go(self):
        tex = get_directory_files(self.texture_dir)
        tex_path = tex[0]
        tex_name = tex[1]
        index = 0
        if self.ui.T_name.text() != "":
            for name in tex_name:
                tex_type = get_texture_type(name)
                tex_res = get_tex_res(name)
                new_tex_name = self.ui.T_name.text() + "_" + tex_type + "_" + tex_res + "." + name.split(".")[-1]
                print(new_tex_name)
                rename(tex_path[index], new_tex_name)
                index += 1
        else:
            QMessageBox.warning(None, "Warning", "Asset Name is Empty!")


if __name__ == '__main__':
    import sys

    app = QApplication([])
    window = Texture_renamer()
    window.show()
    sys.exit(app.exec_())
