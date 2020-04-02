#this script is used to split a single jpg into four quadrant jpg's
#also useful for order_images.py

import cv2
import os

path = './'

for f in os.listdir(path):
    prefix = f.split('.')[0]
    suffix = f.split('.')[-1]
    if suffix == 'jpg':
        img = cv2.imread(f)
        pic_length = int(img.shape[0])
        for r in range(0,pic_length,int(pic_length/2)):
    	    for c in range(0,pic_length,int(pic_length/2)):
                cv2.imwrite(f"{prefix}img{r}_{c}.jpg",img[r:r+int(pic_length/2), c:c+int(pic_length/2),:])