#!/usr/bin/env python
# Copyright (c) 2008-14 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4.QtCore import Qt
from PyQt4.QtCore import pyqtSignal as Signal
from PyQt4.QtGui import (QApplication, QDialog, QDialogButtonBox,
        QGridLayout, QLabel, QSpinBox)


class ResizeDlg(QDialog):

    def __init__(self, width, height, parent=None):
        super(ResizeDlg, self).__init__(parent)
        self.create_widgets(width, height)
        self.layout_widgets()
        self.create_connections()
        self.setWindowTitle(self.tr("Image Changer - Resize"))


    def create_widgets(self, width, height):
        self.widthLabel = QLabel(self.tr("&Width:"))
        self.widthSpinBox = QSpinBox()
        self.widthLabel.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.widthSpinBox.setRange(4, width * 4)
        self.widthSpinBox.setValue(width)
        self.heightLabel = QLabel(self.tr("&Height:"))
        self.heightSpinBox = QSpinBox()
        self.heightLabel.setBuddy(self.heightSpinBox)
        self.heightSpinBox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.heightSpinBox.setRange(4, height * 4)
        self.heightSpinBox.setValue(height)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|
                                          QDialogButtonBox.Cancel)


    def layout_widgets(self):
        layout = QGridLayout()
        layout.addWidget(self.widthLabel, 0, 0)
        layout.addWidget(self.widthSpinBox, 0, 1)
        layout.addWidget(self.heightLabel, 1, 0)
        layout.addWidget(self.heightSpinBox, 1, 1)
        layout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.setLayout(layout)


    def create_connections(self):
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)


    def result(self):
        return self.widthSpinBox.value(), self.heightSpinBox.value()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = ResizeDlg(64, 128)
    form.show()
    app.exec_()

