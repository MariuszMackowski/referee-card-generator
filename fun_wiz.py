# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:38:57 2019

@author: Mario
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 12:56:24 2019

@author: Mario
"""

import cv2, numpy as np
from PIL import Image, ImageFont, ImageDraw


def format_name(name):
    splited_name = name.split(" ")
    name = splited_name[0].upper()
    for i in range(1,len(splited_name)):
        name = name + splited_name[i]
    return  name

def generuj(napisy):
    ## READ INPUT
    liga = str(napisy[0])
    miejsce = str(napisy[1])
    czas_data = str(napisy[2])
    sedzia = str(napisy[3])
    asystent1 = str(napisy[4])
    asystent2 = str(napisy[5])
    klub_1_nazwa = str(napisy[6])
    logo_1_path = str(napisy[7])
    if not logo_1_path == "":
        logo1 = cv2.imread(logo_1_path)
        logo1 = cv2.resize(logo1, (150,150))
    else:
        logo1 = None
    
    klub_2_nazwa = str(napisy[8])
    logo_2_path = napisy[9]
    if not logo_2_path == "":
        logo2 = cv2.imread(logo_2_path)
        logo2 = cv2.resize(logo2, (150,150))
    else:
        logo2 = None
    
    ## READ BASE IMAGE ##
    orig = cv2.imread("./res/wizytowka.png")
    w_i, h_i = orig.shape[1],orig.shape[0]
    cv2_im_rgb = cv2.cvtColor(orig,cv2.COLOR_BGR2RGB)
    pil_im = Image.fromarray(cv2_im_rgb)
    draw = ImageDraw.Draw(pil_im)
    
    ## FONTS ##
    font = ImageFont.truetype("./res/arial-black.ttf", 20)
    font2 = ImageFont.truetype("./res/arial-italic.ttf", 16)
    font3 = ImageFont.truetype("./res/arial-black.ttf", 16)
    
    ## TEXT WIDTH ##
    w_liga  = draw.textsize(liga.encode('utf-8'))[0]
    w_miejsce  = draw.textsize(miejsce.encode('utf-8'))[0]
    w_czas_data = draw.textsize(czas_data.encode('utf-8'))[0]
    w_sedzia = draw.textsize(sedzia.encode('utf-8'))[0]
    w_asystent1 = draw.textsize(asystent1.encode('utf-8'))[0]
    w_asystent2 = draw.textsize(asystent2.encode('utf-8'))[0]  
    
    
    
    
    ## WRITE TEXT ON IMAGE ##
    draw.text(((w_i - w_liga)/2, 40), liga, font=font, fill=(0,0,0)) 
    draw.text(((w_i - w_miejsce)/2, 80), miejsce, font=font, fill=(0,0,0))
    draw.text(((w_i - w_czas_data)/2+15, 120), czas_data, font=font2, fill=(0,0,0))  
    draw.text(((w_i - w_sedzia)/2, 290), sedzia, font=font3, fill=(0,0,0))  
    draw.text(((w_i - w_asystent1)/2, 330), asystent1, font=font3, fill=(0,0,0))  
    draw.text(((w_i - w_asystent2)/2, 370), asystent2, font=font3, fill=(0,0,0)) 
    draw.text( (w_i * 0.1, h_i*0.4), klub_1_nazwa, font=font, fill=(0,0,0))  
    draw.text( ( w_i * 0.75, h_i*0.4), klub_2_nazwa, font=font, fill=(0,0,0))  
    
    ## ADD LOGOS TO IMAGES
    im_napisany = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
    if logo1 is not  None:
        im_napisany[30:30+logo1.shape[0],30:30+logo1.shape[1]] = logo1
    if logo2 is not None:
        im_napisany[30:30+logo2.shape[0],443:443+logo2.shape[1]] = logo2
    
    ## SHOW && WRITE ##
    cv2.imwrite(napisy[10],im_napisany)
    cv2.imshow('Wizytowka', im_napisany)  
    cv2.waitKey(0)     
    cv2.destroyAllWindows() 
    