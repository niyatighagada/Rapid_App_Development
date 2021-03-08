import cv2
import os
import numpy as np
import faceRecognition as fr
import pandas as pd


#This module takes images  stored in diskand performs face recognition
test_img=cv2.imread("TestImages/niyati.jpg")#test_img path
faces_detected,gray_img=fr.faceDetection(test_img)
print("faces_detected:",faces_detected)

file= "atsheet.csv"
df =pd.read_csv(file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
df=df.fillna("N")

#Comment belows lines after training
faces,faceID=fr.labels_for_training_data('trainingImages')
face_recognizer=fr.train_classifier(faces,faceID)
face_recognizer.write('trainingData.yml')


#Uncomment below line for subsequent runs
#face_recognizer=cv2.face.LBPHFaceRecognizer_create()
#face_recognizer.read('trainingData.yml')

name={0:"sanath", 1:"niyati"}

for face in faces_detected:
    (x,y,w,h)=face
    roi_gray=gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)
    print("confidence:",confidence)
    print("label:",label)
    fr.draw_rect(test_img,face)
    predicted_name=name[label]
    if(confidence>37):
        continue
    fr.put_text(test_img,predicted_name,x,y)
    print(predicted_name)
    conv=str(predicted_name)
    print(conv)
    df.loc[df['Name'] == conv, 'Present'] = 'Y'

df.to_csv("attendance.csv",index=False)
print(df)

resized_img=cv2.resize(test_img,(1000,1000))
cv2.imshow("face detecetion Syestem",resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows





