#this script is used to split a single jpg into n*n quadrant jpg's
#also useful for order_images.py

import cv2
import os

path = './'

n = 3 #this is the number of slides per side, i.e. 3 -> 9 equally sized chunks

for f in os.listdir(path):
    prefix = f.split('.')[0]
    suffix = f.split('.')[-1]
    if suffix == 'jpg':
        img = cv2.imread(f)
        pic_length = int(img.shape[0])
        for r in range(0,n*int(pic_length/n),int(pic_length/n)):
    	    for c in range(0,n*int(pic_length/n),int(pic_length/n)):
                cv2.imwrite(f"{prefix}img{r}_{c}.jpg",img[r:r+int(pic_length/n), c:c+int(pic_length/n),:])