import os
import numpy as np
import cv2
from PIL import Image
from Imagedecrypt import Decrypt

recognizer = cv2.face.LBPHFaceRecognizer_create()
path="c:/Users/Lenovo/Desktop/analiz/test"

imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
for image_path in imagePaths:
    Decrypt(image_path)
    
def getImagesWithID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    faces = []
    IDs = []
    for imagePath in imagePaths:

        facesImg = Image.open(imagePath).convert('L')
        faceNP = np.array(facesImg, 'uint8')
  
        ID= int(os.path.split(imagePath)[-1].split(".")[1])

        faces.append(faceNP)
        IDs.append(ID)
        cv2.imshow("Egitim icin yuzler ekleniyor",faceNP)
        cv2.waitKey(10)
    return np.array(IDs), faces
Ids,faces  = getImagesWithID(path)
recognizer.train(faces,Ids)
recognizer.save("c:/Users/Lenovo/Desktop/analiz/trainingdata.yml")
cv2.destroyAllWindows()
