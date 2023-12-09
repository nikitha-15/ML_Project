

from PyQt5 import QtCore, QtGui, QtWidgets

from create_guesters import create_hand_guesters
from SignDetectionCamera import Ui_SignDetectionCamera
from Train_CNN import build_model
import matplotlib.pyplot as plt
class Ui_Main(object):
    
    def create_gustrs(self):
        create_hand_guesters();
        self.showMessageBox("Information", "Dataset created successfully..!")
        
    def train_model(self):
        build_model()
        self.showMessageBox("Information", "CNN model created successfully..!")


    def signdetection_camera(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_SignDetectionCamera()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
        

    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 529)
        Dialog.setStyleSheet("background-color: rgb(65, 65, 65);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 230, 301, 41))
        self.pushButton.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.train_model)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 320, 301, 41))
        self.pushButton_2.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.signdetection_camera)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 30, 821, 81))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Franklin Gothic Heavy\";")
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(180, 140, 301, 41))
        self.pushButton_4.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(148, 98, 73);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.create_gustrs)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
        self.pushButton.setText(_translate("Dialog", "Train Hand Gesture Dataset"))
        self.pushButton_2.setText(_translate("Dialog", "Hand-Sign Recognition"))

        self.label.setText(_translate("Dialog", "Hand-Sign  Recognition using Machine Learning"))
        self.pushButton_4.setText(_translate("Dialog", "Create Hand Gestures"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Main()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
