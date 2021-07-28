# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_bytesasbits.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from led import Led


class Ui_BytesAsBits(object):
    def setupUi(self, BytesAsBits):
        if not BytesAsBits.objectName():
            BytesAsBits.setObjectName(u"BytesAsBits")
        BytesAsBits.resize(213, 340)
        self.verticalLayout = QVBoxLayout(BytesAsBits)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.led0 = Led(BytesAsBits)
        self.led0.setObjectName(u"led0")
        self.led0.setMinimumSize(QSize(31, 31))
        self.led0.setMaximumSize(QSize(31, 31))

        self.gridLayout.addWidget(self.led0, 0, 0, 1, 1)

        self.label1 = QLabel(BytesAsBits)
        self.label1.setObjectName(u"label1")
        self.label1.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label1, 0, 1, 1, 1)

        self.led1 = Led(BytesAsBits)
        self.led1.setObjectName(u"led1")
        self.led1.setMinimumSize(QSize(31, 31))
        self.led1.setMaximumSize(QSize(31, 31))

        self.gridLayout.addWidget(self.led1, 1, 0, 1, 1)

        self.label2 = QLabel(BytesAsBits)
        self.label2.setObjectName(u"label2")
        self.label2.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label2, 1, 1, 1, 1)

        self.led2 = Led(BytesAsBits)
        self.led2.setObjectName(u"led2")
        self.led2.setMinimumSize(QSize(31, 31))
        self.led2.setMaximumSize(QSize(31, 31))

        self.gridLayout.addWidget(self.led2, 2, 0, 1, 1)

        self.label3 = QLabel(BytesAsBits)
        self.label3.setObjectName(u"label3")
        self.label3.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label3, 2, 1, 1, 1)

        self.led3 = Led(BytesAsBits)
        self.led3.setObjectName(u"led3")
        self.led3.setMinimumSize(QSize(31, 31))
        self.led3.setMaximumSize(QSize(31, 31))

        self.gridLayout.addWidget(self.led3, 3, 0, 1, 1)

        self.label4 = QLabel(BytesAsBits)
        self.label4.setObjectName(u"label4")
        self.label4.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label4, 3, 1, 1, 1)

        self.led4 = Led(BytesAsBits)
        self.led4.setObjectName(u"led4")
        self.led4.setMinimumSize(QSize(31, 31))
        self.led4.setMaximumSize(QSize(31, 31))

        self.gridLayout.addWidget(self.led4, 4, 0, 1, 1)

        self.label5 = QLabel(BytesAsBits)
        self.label5.setObjectName(u"label5")
        self.label5.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label5, 4, 1, 1, 1)

        self.led5 = Led(BytesAsBits)
        self.led5.setObjectName(u"led5")
        self.led5.setMinimumSize(QSize(31, 31))
        self.led5.setMaximumSize(QSize(31, 31))

        self.gridLayout.addWidget(self.led5, 5, 0, 1, 1)

        self.label6 = QLabel(BytesAsBits)
        self.label6.setObjectName(u"label6")
        self.label6.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label6, 5, 1, 1, 1)

        self.led6 = Led(BytesAsBits)
        self.led6.setObjectName(u"led6")
        self.led6.setMinimumSize(QSize(31, 31))
        self.led6.setMaximumSize(QSize(31, 31))

        self.gridLayout.addWidget(self.led6, 6, 0, 1, 1)

        self.label7 = QLabel(BytesAsBits)
        self.label7.setObjectName(u"label7")
        self.label7.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label7, 6, 1, 1, 1)

        self.led7 = Led(BytesAsBits)
        self.led7.setObjectName(u"led7")
        self.led7.setMinimumSize(QSize(31, 31))
        self.led7.setMaximumSize(QSize(31, 31))

        self.gridLayout.addWidget(self.led7, 7, 0, 1, 1)

        self.label8 = QLabel(BytesAsBits)
        self.label8.setObjectName(u"label8")
        self.label8.setStyleSheet(u"font: 700 11pt \"Segoe UI\";")

        self.gridLayout.addWidget(self.label8, 7, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(BytesAsBits)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 8, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(BytesAsBits)
        self.buttonBox.accepted.connect(BytesAsBits.accept)
        self.buttonBox.rejected.connect(BytesAsBits.reject)

        QMetaObject.connectSlotsByName(BytesAsBits)
    # setupUi

    def retranslateUi(self, BytesAsBits):
        BytesAsBits.setWindowTitle(QCoreApplication.translate("BytesAsBits", u"BytesAsBits", None))
        self.led0.setProperty("address", QCoreApplication.translate("BytesAsBits", u"'0'", None))
        self.label1.setText(QCoreApplication.translate("BytesAsBits", u"Bit0", None))
        self.led1.setProperty("address", QCoreApplication.translate("BytesAsBits", u"'0'", None))
        self.label2.setText(QCoreApplication.translate("BytesAsBits", u"Bit1", None))
        self.led2.setProperty("address", QCoreApplication.translate("BytesAsBits", u"'0'", None))
        self.label3.setText(QCoreApplication.translate("BytesAsBits", u"Bit2", None))
        self.led3.setProperty("address", QCoreApplication.translate("BytesAsBits", u"'0'", None))
        self.label4.setText(QCoreApplication.translate("BytesAsBits", u"Bit3", None))
        self.led4.setProperty("address", QCoreApplication.translate("BytesAsBits", u"'0'", None))
        self.label5.setText(QCoreApplication.translate("BytesAsBits", u"Bit4", None))
        self.led5.setProperty("address", QCoreApplication.translate("BytesAsBits", u"'0'", None))
        self.label6.setText(QCoreApplication.translate("BytesAsBits", u"Bit5", None))
        self.led6.setProperty("address", QCoreApplication.translate("BytesAsBits", u"'0'", None))
        self.label7.setText(QCoreApplication.translate("BytesAsBits", u"Bit6", None))
        self.led7.setProperty("address", QCoreApplication.translate("BytesAsBits", u"'0'", None))
        self.label8.setText(QCoreApplication.translate("BytesAsBits", u"Bit7", None))
    # retranslateUi

