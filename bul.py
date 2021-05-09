import cv2
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
rec=cv2.face.LBPHFaceRecognizer_create();
rec.read("trainingData.yml")

id=0

fontface=cv2.FONT_HERSHEY_SIMPLEX

while(True):

    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(id==1):
            id="Hasan"
        if id==2:
            id="Firat"
        if id==3:
            id="Hamza"
        if id==4:
            id="Ramazan"  

        cv2.putText(img,str(id),(x,y+h),fontface,2,(255,0,0),3);
    cv2.imshow("Face",img);
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()