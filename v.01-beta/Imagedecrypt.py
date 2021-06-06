import cv2 
import os 
key = 42

def Decrypt(image_path):
    
    image_path = r"{}".format(image_path)
    
    img_reader = open(image_path,'rb')
    image = img_reader.read()
    img_reader.close()
    
    image = bytearray(image)

    for index, values in enumerate(image):
        image[index] = values ^ key
    
     
    decrypt_img = open(image_path, 'wb')
    decrypt_img.write(image)
    decrypt_img.close()
    
    return "Image Decrypt Success"
    

#print(Decrypt('/home/ibex/Desktop/Firat_Doc/analiz/train/User.5.1.jpg'))