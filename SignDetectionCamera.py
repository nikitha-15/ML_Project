# -*- coding: utf-8 -*-





from PyQt5 import QtCore, QtGui, QtWidgets

from Detection_Camera import sign_detection
class Ui_SignDetectionCamera(object):

    def detection(self,event):
        sign_detection()
        event.accept()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(631, 457)
        Dialog.setStyleSheet("background-color: rgb(170, 85, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 50, 411, 51))
        self.label.setStyleSheet("font: 75 16pt \"Vani\";")
        self.label.setObjectName("label")
        self.camera = QtWidgets.QLabel(Dialog)
        self.camera.setGeometry(QtCore.QRect(220, 150, 161, 121))
        self.camera.setStyleSheet("image: url(camera.png);")
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.camera.mousePressEvent = self.detection
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(240, 280, 181, 41))
        self.label_5.setStyleSheet("font: 75 12pt \"Vani\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Hand-Sign  Recognition using Camera"))
        self.label_5.setText(_translate("Dialog", "Click on Camera"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
