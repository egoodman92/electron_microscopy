#this script will relabel all images in your directory
import os
import random
import cv2
import shutil

n = 2 #this is the number of slides per side, i.e. 3 -> 9 equally sized chunks

path = './'

#list of files in the path
files = [f for f in os.listdir('./') if os.path.isfile(f)]

#randomly shuffle indices
indices = [i for i in range(1, n*n*(len(files) - 1) + 1)] #removed one because of this script!
random.shuffle(indices)
print('length of indices is', len(indices), 'and len files is', len(files))

counter = 0 #used for indexing pictures
for f in files:
    saved_name = f
    prefix = f.split('.')[0]
    suffix = f.split('.')[-1]
    if suffix == 'jpg':
        img = cv2.imread(f)
        pic_length = int(img.shape[0])
        for r in range(0,n*int(pic_length/n),int(pic_length/n)):
    	    for c in range(0,n*int(pic_length/n),int(pic_length/n)):
                cv2.imwrite(str(indices[counter])+".jpg",img[r:r+int(pic_length/n), c:c+int(pic_length/n),:])
                print('Labeling image {} from image {}'.format(indices[counter], saved_name))
                counter += 1
        if os.path.exists(f):
            os.remove(f)

train_path = os.path.join(path, 'train')
os.mkdir(train_path)
val_path = os.path.join(path, 'val')
os.mkdir(val_path)
test_path = os.path.join(path, 'test')
os.mkdir(test_path)

cropped_files = [f for f in os.listdir('./') if os.path.isfile(f)]
for cf in cropped_files:
    prefix = cf.split('.')[0]
    suffix = cf.split('.')[-1]
    if suffix == 'jpg':
        if int(prefix) <= 115:
            shutil.move(path+cf, test_path + '/' + cf)
        elif int(prefix) <= 230:
            shutil.move(path+cf, val_path + '/' + cf)
        else:
            shutil.move(path+cf, train_path + '/' + cf)


