# -*- coding: utf-8 -*-
import sys

from PySide6 import QtWidgets

from bytesasbits import BytesAsBits


def main():
    app = QtWidgets.QApplication(sys.argv)

    mw = BytesAsBits()
    mw.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
