#### Developed by Ojas Joshi #####
import cv2
import numpy as np
import os

def readFile(path):
    return open(path, 'rt')

def load_images_from_folder(folder):
    images_list = {}
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename),0)
        if img is not None:
            images_list[filename]=img
    return images_list

def load_centers(images_list, inputString):
	images_data = []
	for line in inputString.splitlines():
		line = line.split()
		images_data.append((images_list[line[0]],float(line[1]),float(line[2]), line[0][0:len(line[0])-4]))
	return images_data

def make_labels(filepath):

	inputFile = readFile(filepath+"labels.txt")
	inputString = inputFile.read()

	images_list = load_images_from_folder(filepath)
	images_data = load_centers(images_list, inputString)
	
	for imgs in images_data: 
		train = []

		img = imgs[0]
		img_true = img

		img = cv2.bilateralFilter(img,9,75,75)

		center = (imgs[1],imgs[2])
		height, width = img.shape
		x = int(center[0]*width)
		y = int(center[1]*height)
		h = 40
		w = 40
		img = img[max(y-h,0):min(y+h,height), max(x-h,0):min(x+w,width)]
		
		
		edges = cv2.Canny(img,100,200)
		im2, cs, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		max_area = np.NINF
		phone_box = cs[0]
		for c in cs:
			xt,yt,wt,ht = cv2.boundingRect(c)
			if(wt*ht>max_area and wt*ht<w*h):
				max_area = wt*ht
				phone_box = c

		x_r,y_r,wid,hei = cv2.boundingRect(phone_box)

		x_bb = int(center[0]*width) - 40 + x_r + int(wid/2)
		y_bb = int(center[1]*height) - 40 + y_r + int(hei/2)

		wid *= 1.1
		hei *= 1.1

		train.append((0,x_bb/width,y_bb/height,wid/width,hei/height))

		tf = open(filepath+'/'+imgs[3]+'.txt', 'w')
		for item in train:
			line = ' '.join(str(x) for x in item)
			tf.write(line + '\n')


		# img_true = cv2.rectangle(img_true,(x_bb-int(wid/2),y_bb-int(hei/2)),(x_bb+int(wid/2),y_bb+int(hei/2)),(0,255,0),2)
		# cv2.circle(img_true, (x_bb,y_bb), 1, (255, 0, 0), -1)

		# cv2.imshow("image",img_true)
		# cv2.waitKey(1000)
