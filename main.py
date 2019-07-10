#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

This program centers a window
on the screen.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017

"""
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QMessageBox, QHBoxLayout, QVBoxLayout, QPushButton, \
    QAction, QLabel, QInputDialog


class Application(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(1000, 600)
        self.center()
        self.getInteger()
        self.setInterface()
        self.setWindowTitle('PROJET OPTIMISATION')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def setInterface(self):
        RUNButton = QPushButton("RUN")
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(RUNButton)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        #menu vertical gauche
        vMenuG = QVBoxLayout()
        bbAction = QAction('Branch & Bound', self)
        H1Action = QAction('Heuristique 1', self)
        H2Action = QAction('Heuristique 2', self)
        H3Action = QAction('Heuristique 3', self)
        NEHAction = QAction('Heuristique NEH', self)
        AGAction = QAction('Algorithme génétique', self)
        VNSAction = QAction('MetaHeuristique VNS', self)
        HHAction = QAction('Hyper heuristique', self)
        """vMenuG.addWidget(bbAction)
        vMenuG.addWidget(H1Action)
        vMenuG.addWidget(H2Action)
        vMenuG.addWidget(H3Action)
        vMenuG.addWidget(NEHAction)
        vMenuG.addWidget(AGAction)
        vMenuG.addWidget(VNSAction)
        vMenuG.addWidget(HHAction)
        """
        #menu vertical droit
        vMenuD = QVBoxLayout()
        #Application Layout
        hbox = QHBoxLayout()
        hbox.addLayout(vMenuG)
        hbox.addLayout(vMenuD)


        instance = QLabel('Instance')
        machine= QLabel('Machine')
        job = QLabel('JOB')



        self.setLayout(hbox)

    def getInteger(self):
        i, okPressed = QInputDialog.getInt(self, "Get integer", "Percentage:", 28, 0, 100, 1)
        if okPressed:
            print(i)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())

# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program creates a menubar. The
menubar has one menu with an exit action.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: January 2017
"""
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def setInterface(self):
        bbAction = QAction('Branch & Bound',self)
        H1Action = QAction('Heuristique 1', self)
        H2Action = QAction('Heuristique 2', self)
        H3Action = QAction('Heuristique 3', self)
        NEHAction = QAction('Heuristique NEH', self)
        AGAction = QAction('Algorithme génétique', self)
        VNSAction = QAction('MetaHeuristique VNS', self)
        HHAction = QAction('Hyper heuristique', self)



    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
"""