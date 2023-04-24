from PyQt5 import QtCore, QtGui, QtWidgets


class uiScanning(object):
    def setup_ui(self, Scanning):
        Scanning.setObjectName("Scanning")
        Scanning.resize(872, 691)
        self.btn_start = QtWidgets.QPushButton(Scanning)
        self.btn_start.setGeometry(QtCore.QRect(530, 510, 201, 71))
        self.btn_start.setObjectName("btn_start")
        self.label_3 = QtWidgets.QLabel(Scanning)
        self.label_3.setGeometry(QtCore.QRect(90, 350, 261, 121))
        font = QtGui.QFont()
        font.setFamily("Modern No. 20")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Scanning)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(90, 450, 241, 191))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.choose_algorythm_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.choose_algorythm_layout.setContentsMargins(0, 0, 0, 0)
        self.choose_algorythm_layout.setObjectName("choose_algorythm_layout")
        self.radbtn_show_graph = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radbtn_show_graph.setFont(font)
        self.radbtn_show_graph.setObjectName("radbtn_show_graph")
        self.choose_algorythm_layout.addWidget(self.radbtn_show_graph, 0, 0, 1, 1)
        self.status_label = QtWidgets.QLabel(Scanning)
        self.status_label.setGeometry(QtCore.QRect(500, 480, 241, 41))
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.scanned_image_label = QtWidgets.QLabel(Scanning)
        self.scanned_image_label.setGeometry(QtCore.QRect(44, 55, 381, 321))
        self.scanned_image_label.setObjectName("scanned_image_label")
        self.label_2 = QtWidgets.QLabel(Scanning)
        self.label_2.setGeometry(QtCore.QRect(580, 250, 55, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslate_ui(Scanning)
        QtCore.QMetaObject.connectSlotsByName(Scanning)

    def retranslate_ui(self, Scanning):
        _translate = QtCore.QCoreApplication.translate
        Scanning.setWindowTitle(_translate("Scanning", "Form"))
        self.btn_start.setText(_translate("Scanning", "Go"))
        self.label_3.setText(_translate("Scanning", "Выполнить:"))
        self.radbtn_show_graph.setText(_translate("Scanning", "Show Graph"))
        self.scanned_image_label.setText(_translate("Scanning", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Scanning = QtWidgets.QWidget()
    ui = uiScanning()
    ui.setup_ui(Scanning)
    Scanning.show()
    sys.exit(app.exec_())
