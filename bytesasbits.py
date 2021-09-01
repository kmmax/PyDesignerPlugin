# -*- coding: utf-8 -*-
import sys

from PySide6 import QtCore, QtWidgets

from ui_bytesasbits import Ui_BytesAsBits


class BytesAsBits(QtWidgets.QDialog):
    """This class represents simple form is created by PySide6-Designer"""
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_BytesAsBits()
        self.ui.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)

    mw = BytesAsBits()
    mw.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
