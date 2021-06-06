import os
import cv2
import numpy as np


key = 42

def Encrypt(img_path):
				
	img_reader = open(img_path,'rb')
	image = img_reader.read()
	img_reader.close()
	
	image = bytearray(image)

	for index,values in enumerate(image):
		image[index] = values ^ key
	
	
	new_file = open(img_path, 'wb')
	new_file.write(image)
	new_file.close()
		
	return "Image Encrypt Success"