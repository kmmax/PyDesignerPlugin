#############################################################################
##
## Copyright (C) 2021 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the Qt for Python examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################

from PySide6.QtCore import Qt, QPoint, QRect, QSize, Property, Slot
from PySide6.QtGui import QMouseEvent, QPainter, QPen
from PySide6.QtWidgets import QWidget

from PySide6.QtWidgets import QApplication
from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal, Slot


class Led(QLabel):
    """The Led is custom widget for PySide6-designer

    He is round led with 2 color states. By clicking it changes his state.
    """
    def __init__(self, parent=None):
        super(Led, self).__init__(parent)
        self.__pix_on = QtGui.QPixmap("green_led.png")
        self.__pix_off = QtGui.QPixmap("red_led.png")
        self.__value = False
        self.setValue(self.__value)
        self.init()

    def init(self):
        self.setScaledContents(True)
        # self.setText("My Label")
        self.updateGui()
        self.resize(100, 100)

    @Slot(int)
    def onValueUpdate(self, value):
        if value > 50:
            self.setValue(True)
        else:
            self.setValue(False)

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        self.setValue(not self.__value)

    @Slot(bool)
    def setValue(self, value):
        self.__value = value
        self.updateGui()

    def updateGui(self):
        if self.__value:
            self.setPixmap(self.__pix_on)
        else:
            self.setPixmap(self.__pix_off)
