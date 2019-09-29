# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:20:11 2019

@author: Mario
"""
#from PyQt5.QtWidgets import QLineEdit
#import cv2, numpy as np
#from PIL import Image, ImageFont, ImageDraw
#
#line = QLineEdit("ąćź")
#
#
#
#orig = cv2.imread("wizytowka.png")
#w_i, h_i = orig.shape[1],orig.shape[0]
#cv2_im_rgb = cv2.cvtColor(orig,cv2.COLOR_BGR2RGB)
#pil_im = Image.fromarray(cv2_im_rgb)
#draw = ImageDraw.Draw(pil_im)
#
#
#liga = line.text()
#w_liga  = draw.textsize(liga.encode('utf-8'),language="PL")[0]
#print(liga)
#print(w_liga)





def format_name(name):
    splited_name = name.split(" ")
    return splited_name[0].upper() + " " + splited_name[1]


name = "Salos Szczecin"
print(format_name(name))