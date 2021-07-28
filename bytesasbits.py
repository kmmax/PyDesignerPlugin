# -*- coding: utf-8 -*-

from PySide6 import QtCore, QtWidgets
import sys

import ui_bytesasbits
from ui_bytesasbits import Ui_BytesAsBits


class BytesAsBits(QtWidgets.QDialog):
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
