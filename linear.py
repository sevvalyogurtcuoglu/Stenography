# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 00:26:49 2019

@author: TOSHIBA
"""

import cv2
import numpy as np
image=cv2.imread("twe.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#dim = (512, 512)
resize=cv2.resize(gray, (512,512))
# mesajın acsii ye dönüştüülmesi
 
c = 0
for s in "sevval":
    c += 1
print(c)

b=c*8

ascii_value=[ord(ch) for ch in "sevval"]
print(ascii_value)
#%% binary sisteme dönüştürme

aa=bin(115)
result = []
for i in ascii_value:
    result.append(bin(i))

bin_message = [int(x) if x.isdigit() else x  
          for z in result for x in str(z)]
#bin_message_len=len(bin_message)
n = 0
for d in bin_message:
    n += 1
print(n)
#%%
output=resize
h, w = resize.shape
bbb=[h,w]
embed_counter = 1


for e in range(h):
    for j in range(w):
        if(embed_counter <= b):
            LSB =np.mod((bbb), 2)
            temp1=LSB^LSB
            g=[n*embed_counter]
            temp = (LSB ^ g)
            output = resize[e][j]+temp
            
            embed_counter = embed_counter+1
  
    
  
cv2.imshow('image',resize)
cv2.imshow('output',output)



cv2.waitKey(0)
cv2.destroyAllWindows()# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

