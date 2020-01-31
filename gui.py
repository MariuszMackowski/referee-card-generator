# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 11:31:27 2019

@author: Mario
"""

from functools import partial
import sys, easygui
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                              QGridLayout, QApplication, QPushButton)

from PyQt5 import QtGui, QtCore
import fun_wiz
import scrap

class Example(QWidget):

    def __init__(self):
        super().__init__()
        
        ## Labels
        self.label_liga = QLabel('Liga: ')
        self.label_miejsce = QLabel('Miejsce: ')
        self.label_czas_data = QLabel('Czas i data:')
        self.label_sedzia = QLabel("Sędzia: ")
        self.label_asystent_1 = QLabel("Asystent 1:")
        self.label_asystent_2 = QLabel("Asystent 2:")
        self.label_klub_1_nazwa= QLabel('Klub 1 nazwa:')
        self.label_klub_1_logo= QLabel('Klub 1 logo:')
        self.label_klub_2_nazwa= QLabel('Klub 2 nazwa:')
        self.label_klub_2_logo= QLabel('Klub 2 logo:')
        self.label_zapis= QLabel('Zapis:')
        self.label_link= QLabel('Link:')

        ## LineEdits
        self.edit_liga = QLineEdit()
        self.edit_miejsce = QLineEdit()
        self.edit_czas_data = QLineEdit()
        self.edit_sedzia = QLineEdit()
        self.edit_asystent_1 = QLineEdit()
        self.edit_asystent_2 = QLineEdit()
        self.edit_klub_1_nazwa= QLineEdit()
        self.edit_klub_1_logo= QLineEdit()
        self.edit_klub_2_nazwa= QLineEdit()
        self.edit_klub_2_logo= QLineEdit()
        self.edit_zapis= QLineEdit("wiz.png")
        self.edit_link= QLineEdit()
        
        ## Buttons
        self.bn_generuj = QPushButton("Generuj",self)
        self.bn_logo_1_path = QPushButton(self)
        self.bn_logo_2_path= QPushButton(self)
        self.bn_zapis_path= QPushButton(self)
        self.bn_sciagnij = QPushButton("Sciagnij", self)
        
        ## Buttons icons
        self.bn_logo_1_path.setIcon(QtGui.QIcon('./res/folder.png'))
        self.bn_logo_1_path.setIconSize(QtCore.QSize(16,16))
        
        self.bn_logo_2_path.setIcon(QtGui.QIcon('./res/folder.png'))
        self.bn_logo_2_path.setIconSize(QtCore.QSize(16,16))
        
        self.bn_zapis_path.setIcon(QtGui.QIcon('./res/folder.png'))
        self.bn_zapis_path.setIconSize(QtCore.QSize(16,16))
        
        ## Buttons Connections
        self.bn_generuj.clicked.connect(self.button_generate)
        self.bn_logo_1_path.clicked.connect(partial(self.button_path,self.edit_klub_1_logo))
        self.bn_logo_2_path.clicked.connect(partial(self.button_path,self.edit_klub_2_logo))
        self.bn_zapis_path.clicked.connect(partial(self.button_save,self.edit_zapis))
        self.bn_sciagnij.clicked.connect(self.button_download)
        
        ## Layout
        grid = QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(self.label_link,0,0)
        grid.addWidget(self.edit_link,0,1)
        
        grid.addWidget(self.bn_sciagnij,1,0,1,3)
        
        grid.addWidget(self.label_liga,2,0)
        grid.addWidget(self.edit_liga,2,1)

        grid.addWidget(self.label_miejsce,3,0)
        grid.addWidget(self.edit_miejsce,3,1)
        
        grid.addWidget(self.label_czas_data,4,0)
        grid.addWidget(self.edit_czas_data,4,1)
        
        grid.addWidget(self.label_sedzia,5,0)
        grid.addWidget(self.edit_sedzia,5,1)
        
        grid.addWidget(self.label_asystent_1,6,0)
        grid.addWidget(self.edit_asystent_1,6,1)
        
        grid.addWidget(self.label_asystent_2,7,0)
        grid.addWidget(self.edit_asystent_2,7,1)
        
        grid.addWidget(self.label_klub_1_nazwa,8,0)
        grid.addWidget(self.edit_klub_1_nazwa,8,1)
        
        grid.addWidget(self.label_klub_1_logo,9,0)
        grid.addWidget(self.edit_klub_1_logo,9,1)
        grid.addWidget(self.bn_logo_1_path ,9,2)

        
        grid.addWidget(self.label_klub_2_nazwa,10,0)
        grid.addWidget(self.edit_klub_2_nazwa,10,1)
        
        grid.addWidget(self.label_klub_2_logo,11,0)
        grid.addWidget(self.edit_klub_2_logo,11,1)
        grid.addWidget(self.bn_logo_2_path ,11,2)
        
        grid.addWidget(self.label_zapis,12,0)
        grid.addWidget(self.edit_zapis,12,1)
        grid.addWidget(self.bn_zapis_path, 12,2)
        
        grid.addWidget(self.bn_generuj,13,0,1,3)
        
        
        
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Wizytowka')
        self.show()
      
        ## Button functions        
        
    def button_download(self):
        ## Scrap info from provided url. Fills EditLines.
        url = self.edit_link.text()
        if url != "":
            names = scrap.download_info(url)
            print(names)
            self.edit_klub_1_nazwa.setText(fun_wiz.format_name(names[0]))
            self.edit_klub_2_nazwa.setText(fun_wiz.format_name(names[1]))
            self.edit_czas_data.setText(names[2])
            self.edit_miejsce.setText(names[3])
            self.edit_klub_1_logo.setText(names[4])
            self.edit_klub_2_logo.setText(names[5]) 

    def button_path(self, line_edit):
        ## Opens file dialog to provide clubs logos
        text = easygui.fileopenbox()
        line_edit.setText(text)
        
    def button_save(self, line_edit):
        ## Opens file dialog to get save location
        text = easygui.filesavebox()
        line_edit.setText(text)
        
        
    def button_generate(self):
        ## Gather info from EditLines to generate card
        napisy = [
                str(self.edit_liga.text()),
                str(self.edit_miejsce.text()),
                str(self.edit_czas_data.text()),
                str(self.edit_sedzia.text()),
                str(self.edit_asystent_1.text()),
                str(self.edit_asystent_2.text()),
                str(self.edit_klub_1_nazwa.text()).replace("  ", "\n"),
                str(self.edit_klub_1_logo.text()).replace("\\" ,"\\\\"),
                str(self.edit_klub_2_nazwa.text()).replace("  ", "\n"),
                str(self.edit_klub_2_logo.text()).replace("\\" ,"\\\\"),
                str(self.edit_zapis.text()),
                    ]
        fun_wiz.generuj(napisy)
        

        
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
