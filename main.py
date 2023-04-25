import sys, os
from shutil import copyfile

import networkx as nx
import cv2
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel, QPushButton, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QPixmap

import build
from pyqt.bar import uiMainWindow
from pyqt.scanned import uiScanning
from pyqt.show import uiOutputWindow


class MainWindow(QtWidgets.QMainWindow, uiMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.show()
        self.file = None
        self.btn_image.clicked.connect(self.add_file)  # !!! +++
        self.btn_scan.clicked.connect(self.scan_file)

    @QtCore.pyqtSlot()
    def add_file(self):
        fname, filetype = QFileDialog.getOpenFileName(
            self,
            "Open file",
            ".",
            "Images (*.jpg, *.png);;"
        )

        self.write_status(fname)
        pixmap = QPixmap(fname)
        w = pixmap.width()
        h = pixmap.height()
        d = max(w, h)
        div = d / 320
        resized = pixmap.scaled(w // div, h / div)
        self.image_label.setPixmap(resized)
        self.file = fname

    def scan_file(self):
        if self.file is not None:

            self.window = ScannedWindow(self.file)
            # self.window.show()
        else:
            self.status_label.setText("file not selected")

    def write_status(self, fname):
        text = "File " + fname + "\nwas readen"
        self.status_label.setText(text, )

class ScannedWindow(QtWidgets.QMainWindow, uiScanning):
    def __init__(self, file):
        super().__init__()
        self.setup_ui(self)
        self.file = file
        self.show()
        self.btn_start.clicked.connect(self.give_output)
        image = cv2.imread(self.file)
        self.graph = build.build_graph(image)
        try:
            self.create_scroll_area()
        except:
            print('create scroll area error')
        self.show_scanned()
        try:
            self.confirm_btn.clicked.connect(self.show_scanned)
        except:
            print("rename error")
    def give_output(self):
        if (self.radbtn_show_graph.isChecked()):
            res = ''
            if (self.radbtn_bfs.isChecked()):
                res = "bfs"
            elif (self.radbtn_dfs.isChecked()):
                res = "dfs"
            elif (self.radbtn_show_graph.isChecked()):
                res = "show"

            self.window = OutputWindow(self.file, self.graph, self.names)
            self.status_label.setText("")
        else:
            self.status_label.setText("Выберите режим работы")

    def show_scanned(self):
        # Достаем изображение и рисуем на нём сканнированный граф
        image = cv2.imread(self.file)
        copyfile(self.file, "scanned_image.png")
        build.write_graph(self.graph, image, "scanned_image.png", self.names)
        pixmap = QPixmap("scanned_image.png")
        w = pixmap.width()
        h = pixmap.height()
        d = max(w, h)
        div = d / 320
        resized = pixmap.scaled(w // div, h // div)
        self.scanned_image_label.setPixmap(resized)
        try:
            # pass
            self.show_scroll_area()
        except:
            print('show scroll area error')
        self.show()
        os.remove("scanned_image.png")

    def create_scroll_area(self):
        self.names = {}
        cnt = 1
        nodes = self.graph.nodes
        vbox = self.node_layout
        for node in nodes:
            line_edit = QLineEdit(f'{cnt}')
            cnt += 1
            self.names[node] = line_edit
            vbox.addWidget(line_edit)
        self.setLayout(vbox)
    def show_scroll_area(self):
        for node in self.graph.nodes:
            print(f'new name: {self.names[node].text()}')

class OutputWindow(QtWidgets.QMainWindow, uiOutputWindow):
    def __init__(self, file, graph, names):
        super().__init__()
        self.setup_ui(self)
        self.file = file
        self.graph = graph
        self.names = names
        self.show()
        # if (key == "bfs"):
        #     # # print("ES")
        #     # s = (self.graph.nodes[0].center.x, self.graph.nodes[0].center.y)
        #     # print(self.graph.nodes)
        #     self.do_bfs()
        # elif (key == "dfs"):
        #     self.do_dfs()
        # elif (key == 'show'):
        #     self.show_clear_graph()
        self.show_clear_graph()
        # self.show()

    def do_bfs(self):
        # print("YES")
        # pos = {}
        # cnt = 1
        # for node in self.graph.nodes:
        #     pos[node] = (node.center.x, node.center.y)
        #     plt.text(node.center.x, node.center.y, "{}".format(cnt))
        #     cnt += 1
        pos = nx.planar_layout(self.graph)
        source = (self.graph.nodes[0].center.x, self.graph.nodes[0].center.y)

        print("YES")
        nx.draw(self.graph, pos, with_labels=True, node_color="#f86e00")


        bfs = nx.bfs_tree(self.graph, source=source)

        nx.draw(bfs, pos, with_labels=True, node_color="#f86e00", edge_color="#dd2222")

        plt.savefig("output_image.png")
        pixmap = QPixmap("output_image.png")
        w = pixmap.width()
        h = pixmap.height()
        d = max(w, h)
        div = d / 300
        resized = pixmap.scaled(w // div, h // div)
        self.output_label.setPixmap(resized)
        os.remove("output_image.png")
        # self.show()

    def show_clear_graph(self):
        # Создадим словарь node : координаты
        pos = {}
        for node in self.graph.nodes:
            pos[node] = (node.center.x, node.center.y)
            plt.text(node.center.x, node.center.y, self.names[node].text())

        # Красивости графа
        options = {
            'node_color': 'blue',  # color of node
            'node_size': 2000,  # size of node
            'width': 3,  # line width of edges
            'edge_color': 'black',  # edge color
        }

        # Нарисуем граф с помощью networkx.draw
        nx.draw(self.graph, pos, **options)

        # Сохраним нарисованный граф в виде временного файла
        plt.savefig("output_image.png")
        pixmap = QPixmap("output_image.png")

        # Выведем изображение как pixmap
        w = pixmap.width()
        h = pixmap.height()
        d = max(w, h)
        div = d / 800
        resized = pixmap.scaled(w // div, h // div)
        self.output_label.setPixmap(resized)
        os.remove("output_image.png")
        self.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    check = MainWindow()
    sys.exit(app.exec_())