#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Loading Images for Swaping
nobita = cv2.imread('nobita.png')
sizuka = cv2.imread('sizuka.png')

# Displaying Loaded Nobita Face
cv2.imshow('Nobita', nobita)
cv2.waitKey(10)
cv2.destroyAllWindows()

# Displaying Loaded Sizuka Face
cv2.imshow('Sizuka', sizuka)
cv2.waitKey(10)
cv2.destroyAllWindows()

# Swaping Sizuka Face on Nobita Body
# Croping Sizuka Face
s = sizuka[30:490,130:670]  
cv2.line(s,(170,450),(305,500),(0,0,0),30)
cv2.line(s,(380,450),(278,500),(0,0,0),70)
cv2.line(s,(550,450),(510,500),(0,0,0),30)
# nobita Body
nb = nobita[670:1600,10:1200] 
width = int(s.shape[1] * 1014/540) 
height = int(s.shape[0] * 930/460)  
dim = (width, height)  
# resize image  
s_resized = cv2.resize(s, dim, interpolation=cv2.INTER_AREA)  
new_sizuka = np.vstack((s_resized,nb))

# Displaying swaped Sizuka Face on Nobita Body
cv2.imshow('New_Sizuka', new_sizuka)
cv2.waitKey(10)
cv2.destroyAllWindows()

# Swaping Nobita Face on Sizuka Body
# Croping Nobita Face
n = nobita[10:670,250:930]
cv2.line(n,(110,650),(210,700),(0,0,0),70)
cv2.line(n,(510,640),(300,700),(0,0,0),80)
# resize image
exl = np.zeros((660,200,3), np.uint8)
nf = np.concatenate((exl,n),axis=1)
width = int(nf.shape[1] * 640/880) 
height = int(nf.shape[0] * 475/660)  
dim = (width, height)
nf_resized = cv2.resize(nf, dim, interpolation=cv2.INTER_AREA)  
sizuka[15:490,10:650] = nf_resized
sizuka[480:550,100:255] = [0,0,0]

# Displaying swaped Nobita Face on Sizuka Body
cv2.imshow('New_Nobita', sizuka)
cv2.waitKey(10)
cv2.destroyAllWindows()
