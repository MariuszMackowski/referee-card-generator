# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 12:56:24 2019

@author: Mario
"""

import cv2, numpy as np, easygui
from PIL import Image, ImageFont, ImageDraw

## INPUT ##
liga = "IV Liga"
miejsce = "Wolin"
czas_data = "21.09.2019 r. godz. 16:00"
sedzia = "Michas"
asystent1 = "Imie Nazwisko"
asystent2 = "Imie Nazwisko"
klub_1_nazwa = "POGON Szczecin".replace(" ", "\n")
klub_2_nazwa = "POGON Szczecin".replace(" ", "\n")

## READ BASE IMAGE ##
orig = cv2.imread("wizytowka.png")
w_i, h_i = orig.shape[1],orig.shape[0]
cv2_im_rgb = cv2.cvtColor(orig,cv2.COLOR_BGR2RGB)
pil_im = Image.fromarray(cv2_im_rgb)
draw = ImageDraw.Draw(pil_im)

## FONTS ##
font = ImageFont.truetype("arial-black.ttf", 20)
font2 = ImageFont.truetype("arial-italic.ttf", 16)

## TEXT WIDTH ##
w_liga  = draw.textsize(liga)[0]
w_miejsce  = draw.textsize(miejsce)[0]
w_czas_data = draw.textsize(czas_data)[0]
w_sedzia = draw.textsize(sedzia)[0]
w_asystent1 = draw.textsize(asystent1)[0]
w_asystent2 = draw.textsize(asystent2)[0]

## READ LOGOS ##
klub_1_logo = None
while klub_1_logo is None:
    klub_1_logo = easygui.fileopenbox()
logo1 = cv2.resize(cv2.imread(klub_1_logo),(150,150))
klub_2_logo = None
while klub_2_logo is None:
    klub_2_logo = easygui.fileopenbox()
logo2 = cv2.resize(cv2.imread(klub_2_logo),(150,150))


## WRITE TEXT ON IMAGE ##
draw.text(((w_i - w_liga)/2, 40), liga, font=font, fill=(0,0,0)) 
draw.text(((w_i - w_miejsce)/2, 80), miejsce, font=font, fill=(0,0,0))
draw.text(((w_i - w_czas_data)/2, 120), czas_data, font=font2, fill=(0,0,0))  
draw.text(((w_i - w_sedzia)/2, 290), sedzia, font=font2, fill=(0,0,0))  
draw.text(((w_i - w_asystent1)/2, 330), asystent1, font=font2, fill=(0,0,0))  
draw.text(((w_i - w_asystent2)/2, 370), asystent2, font=font2, fill=(0,0,0)) 
draw.text( (w_i * 0.1, h_i*0.45), klub_1_nazwa, font=font, fill=(0,0,0))  
draw.text( ( w_i * 0.75, h_i*0.45), klub_2_nazwa, font=font, fill=(0,0,0))  

## ADD LOGOS TO IMAGES
im_napisany = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
im_napisany[30:30+logo1.shape[0],30:30+logo1.shape[1]] = logo1
im_napisany[30:30+logo2.shape[0],443:443+logo2.shape[1]] = logo2

## SHOW && WRITE ##
cv2.imshow('Wizytowka', im_napisany)  
cv2.waitKey(0)     
cv2.destroyAllWindows() 
