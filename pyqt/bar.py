from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class uiMainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 600)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_image = QtWidgets.QPushButton(self.centralwidget)
        self.btn_image.setGeometry(QtCore.QRect(70, 150, 131, 81))
        self.btn_image.setObjectName("btn_image")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(270, 150, 301, 311))
        self.image_label.setObjectName("image_label")
        self.btn_scan = QtWidgets.QPushButton(self.centralwidget)
        self.btn_scan.setGeometry(QtCore.QRect(60, 360, 121, 71))
        self.btn_scan.setObjectName("btn_scan")
        self.radbtn_red = QtWidgets.QRadioButton(self.centralwidget)
        self.radbtn_red.setGeometry(QtCore.QRect(70, 270, 101, 20))
        self.radbtn_red.setObjectName("radbtn_red")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(294, 65, 301, 41))
        self.status_label.setAutoFillBackground(True)
        self.status_label.setLineWidth(56)
        self.status_label.setObjectName("status_label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(400, 60, 71, 41))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "GraphScanner"))
        self.btn_image.setText(_translate("MainWindow", "Image"))
        self.image_label.setText(_translate("MainWindow", "Здесь будет отображатся загруженное изображение"))
        self.btn_scan.setText(_translate("MainWindow", "Scan"))
        self.radbtn_red.setText(_translate("MainWindow", "Red Filter"))
        self.status_label.setText(_translate("MainWindow", "Status:"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = uiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
