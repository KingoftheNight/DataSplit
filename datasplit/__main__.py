import time
import os
file_path = os.path.dirname(__file__)
import sys
sys.path.append(file_path)
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from PyQt5.QtCore import QStringListModel
# 导入UI的所有类
try:
    from . import UI
    from . import create
    from . import open
    from . import standard
    from . import split
    from . import about
    from . import save
    from . import function
except:
    import UI
    import create
    import open
    import standard
    import split
    import about
    import save
    import function
from UI import *
from create import *
from open import *
from standard import *
from split import *
from about import *
from save import *
from function import *


# 创建类
class MyWindow(QMainWindow):

    # 定义功能
    def connect_create(self):
        self.child_create.show()
        self.child_create._signal_create.connect(self.get_create)

    def connect_open(self):
        self.child_open.show()
        self.child_open._signal_open.connect(self.get_open)

    def connect_standard(self):
        self.child_stand.show()
        self.child_stand._signal_standard.connect(self.get_standard)

    def connect_split(self):
        self.child_split.show()
        self.child_split._signal_split.connect(self.get_split)

    def connect_about(self):
        self.child_about.show()

    def connect_save(self):
        self.child_save.show()
        self.child_save._signal_save.connect(self.get_save)

    def click_create(self, index):
        if index.row() == 0:
            content = 'Please choose another file to view!'
        else:
            value = self.qList[index.row()].split('\t')
            file_name = os.path.join(os.path.join(os.path.join(file_path, 'data'), value[1]), value[2])
            with open(file_name, 'r') as f:
                content = f.read()
        self.ui.result_line.setText(content)

    def get_create(self, file_list):
        self.child_create.close()
        self.qList = ['PDB_id\tClass\tfile\tsite'] + file_list
        self.slm.setStringList(self.qList)
        self.listView.setModel(self.slm)
        self.listView.clicked.connect(self.click_create)
        # 给子窗口传递参数
        self.child_split.ui_split.label_main.setText('||'.join(self.qList))

    def get_open(self, folder):
        self.child_open.close()
        file_list = open_data(folder)
        self.ui.result_line.setText('DataBase: ' + folder + '\n\n' + 'Total: ' + str(len(file_list)))
        self.qList = ['PDB_id\tClass\tfile\tsite'] + file_list
        self.slm.setStringList(self.qList)
        self.listView.setModel(self.slm)
        self.listView.clicked.connect(self.click_create)
        # 给子窗口传递参数
        self.child_split.ui_split.label_main.setText('||'.join(self.qList))

    def get_standard(self, file):
        self.child_stand.close()
        out = standard_file(file)
        self.ui.result_line.setText('The standard file has been saved as:\n\n' + out)

    def get_split(self, file_1, file_2, size_1, size_2):
        self.child_split.close()
        data = self.qList
        if file_1 != 'None':
            out_1 = split_data(file_1, size_1, data[1:])
        else:
            out_1 = 'No class has been choosen in class A!'
        if file_2 != 'None':
            out_2 = split_data(file_2, size_2, data[1:])
        else:
            out_2 = 'No class has been choosen in class B!'
        self.ui.result_line.setText('The split file has been saved as:\n\n' + out_1 + '\n' + out_2)

    def get_save(self, file):
        self.child_save.close()
        data = self.qList[1:]
        out_path = save_data(data, name=file.split('.')[0] + '.fasta')
        self.ui.result_line.setText('The select file has been saved as:\n\n' + out_path)

    def search_file(self):
        line = self.ui.search_line.text()
        file_list = search_data(line, self.qList[1:])
        # result
        self.ui.result_line.setText('Sequence in now list: ' + str(len(file_list)))
        # list
        self.qList = ['PDB_id\tClass\tfile\tsite'] + file_list
        self.slm.setStringList(self.qList)
        self.listView.setModel(self.slm)
        self.listView.clicked.connect(self.click_create)
        # 给子窗口传递参数
        self.child_split.ui_split.label_main.setText('||'.join(self.qList))

    def savedata(self):
        data = self.qList[1:]
        out_path = save_data(data)
        self.ui.result_line.setText('The select file has been saved as:\n\n' + out_path)

    # 启动UI
    def __init__(self):
        QMainWindow.__init__(self)
        # 继承
        self.ui = Ui_MainWindow()
        self.setWindowIcon(QtGui.QIcon('./imgs/Logo.ico'))
        self.ui.setupUi(self)
        self.child_create = CreateWindow()
        self.child_open = OpenWindow()
        self.child_stand = StandardWindow()
        self.child_split = SplitWindow()
        self.child_about = AboutWindow()
        self.child_save = SaveWindow()
        # 定义列表
        self.listView = self.ui.search_list
        self.slm = QStringListModel()
        self.qList = ['PDB_id\tClass\tfile\tsite']
        self.slm.setStringList(self.qList)
        self.listView.setModel(self.slm)
        self.listView.clicked.connect(self.click_create)
        # 绑定函数
        self.ui.search_button.clicked.connect(self.search_file)
        self.ui.file_save.triggered.connect(self.savedata)


class CreateWindow(QDialog):
    _signal_create = QtCore.pyqtSignal(list)

    # 定义功能
    def click_load(self):
        file = self.ui_create.create_in_line.text()
        out = self.ui_create.create_out_line.text()
        name = self.ui_create.create_name_line.text()
        if out == '':
            if name == '':
                file_list = load_data(file)
            else:
                file_list = load_data(file, sql=name)
        else:
            if name == '':
                file_list = load_data(file, out=out)
            else:
                file_list = load_data(file, sql=name, out=out)
        self._signal_create.emit(file_list)

    def click_tool(self):
        file = QFileDialog.getOpenFileName(self, os.getcwd())[0]
        self.ui_create.create_in_line.setText(file)
        self.ui_create.create_out_line.setText(os.path.split(file)[-1].split('.')[0])

    def click_tool_2(self):
        file = QFileDialog.getSaveFileName(self, os.getcwd())[0]
        self.ui_create.create_name_line.setText(os.path.split(file)[-1].split('.')[0] + '.csv')

    # 启动UI
    def __init__(self):
        QDialog.__init__(self)
        self.ui_create = Ui_Create()
        self.ui_create.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./imgs/Logo.ico'))
        self.ui_create.create_go_button.clicked.connect(self.click_load)
        self.ui_create.create_tool_button.clicked.connect(self.click_tool)
        self.ui_create.create_tool_button_2.clicked.connect(self.click_tool_2)


class OpenWindow(QDialog):
    _signal_open = QtCore.pyqtSignal(str)

    # 定义功能
    def click_open(self, index):
        value = self.qList_open[index.row()]
        self._signal_open.emit(value)

    # 启动UI
    def __init__(self):
        QDialog.__init__(self)
        self.ui_open = Ui_Open()
        self.ui_open.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./imgs/Logo.ico'))
        self.listView_open = self.ui_open.open_list
        self.slm_open = QStringListModel()
        self.qList_open = os.listdir(os.path.join(file_path, 'list'))
        self.slm_open.setStringList(self.qList_open)
        self.listView_open.setModel(self.slm_open)
        self.listView_open.clicked.connect(self.click_open)


class StandardWindow(QDialog):
    _signal_standard = QtCore.pyqtSignal(str)

    # 定义功能
    def click_standard(self):
        file = self.ui_stand.standard_line.text()
        self._signal_standard.emit(file)

    def fileread_standard(self):
        file = QFileDialog.getOpenFileName(self, os.getcwd())
        self.ui_stand.standard_line.setText(file[0])

    # 启动UI
    def __init__(self):
        QDialog.__init__(self)
        self.ui_stand = Ui_Standard()
        self.ui_stand.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./imgs/Logo.ico'))
        self.ui_stand.standard_button.clicked.connect(self.click_standard)
        self.ui_stand.standard_tool.clicked.connect(self.fileread_standard)


class SplitWindow(QDialog):
    _signal_split = QtCore.pyqtSignal(str, str, str, str)

    # 定义功能
    def click_split(self):
        file_1 = self.ui_split.split_A_line.currentText()
        file_2 = self.ui_split.split_B_line.currentText()
        size_1 = self.ui_split.split_A_size.currentText()
        size_2 = self.ui_split.split_B_size.currentText()
        self._signal_split.emit(file_1, file_2, size_1, size_2)

    def flush_split(self):
        type_list = self.ui_split.label_main.text().split('||')[1:]
        list_type = get_list(type_list)
        self.ui_split.split_A_line.clear()
        self.ui_split.split_B_line.clear()
        self.ui_split.split_A_line.addItems(list_type + ['None'])
        self.ui_split.split_B_line.addItems(list_type + ['None'])

    # 启动UI
    def __init__(self):
        QDialog.__init__(self)
        self.ui_split = Ui_Split()
        self.ui_split.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./imgs/Logo.ico'))
        self.ui_split.label_main
        self.ui_split.split_load_button.clicked.connect(self.flush_split)
        self.ui_split.split_button.clicked.connect(self.click_split)


class AboutWindow(QDialog):

    # 启动UI
    def __init__(self):
        QDialog.__init__(self)
        self.ui_about = Ui_About()
        self.ui_about.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./imgs/Logo.ico'))


class SaveWindow(QDialog):
    _signal_save = QtCore.pyqtSignal(str)

    # function
    def click_save(self):
        file = self.ui_save.save_line.text()
        self._signal_save.emit(file)

    # 启动UI
    def __init__(self):
        QDialog.__init__(self)
        self.ui_save = Ui_Save()
        self.ui_save.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./imgs/Logo.ico'))
        self.ui_save.save_button.clicked.connect(self.click_save)


def datasplit():
    app = QApplication(sys.argv)
    myWin = MyWindow()
    child_create = CreateWindow()
    child_open = OpenWindow()
    child_save = SaveWindow()
    child_standard = StandardWindow()
    child_split = SplitWindow()
    child_about = AboutWindow()
    ct_button = myWin.ui.file_create
    op_button = myWin.ui.file_open
    se_button = myWin.ui.file_saveas
    sd_button = myWin.ui.edit_stand
    st_button = myWin.ui.edit_split
    at_button = myWin.ui.help_about
    ct_button.triggered.connect(myWin.connect_create)
    op_button.triggered.connect(myWin.connect_open)
    se_button.triggered.connect(myWin.connect_save)
    sd_button.triggered.connect(myWin.connect_standard)
    st_button.triggered.connect(myWin.connect_split)
    at_button.triggered.connect(myWin.connect_about)
    # view
    myWin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    datasplit()
