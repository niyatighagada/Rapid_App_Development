import os
import cv2
import numpy as np
import faceRecognition as fr
import pandas as pd 
import pygsheets



face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')

name={0:"sanath", 1:"niyati"}

file= "atsheet.csv"
df =pd.read_csv(file, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
df.fillna("N")
cap=cv2.VideoCapture(0)

while True:
    ret,test_img=cap.read()
    faces_detected,gray_img=fr.faceDetection(test_img)



    for (x,y,w,h) in faces_detected:
      cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)

    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face detection Tutorial ',resized_img)
    cv2.waitKey(10)


    for face in faces_detected:
        (x,y,w,h)=face
        roi_gray=gray_img[y:y+w, x:x+h]
        label,confidence=face_recognizer.predict(roi_gray)
        print("confidence:",confidence)
        print("label:",label)
        fr.draw_rect(test_img,face)
        predicted_name=name[label]
        if confidence < 39:
           fr.put_text(test_img,predicted_name,x,y)

        print(predicted_name)
        conv=str(predicted_name)
        print(conv)
        df.loc[df['Name'] == conv, 'Present'] = 'Y'


    df.fillna('N')
    gc = pygsheets.authorize(service_file='service_key.json') 
    sh = gc.open('falcon')
    wks = sh.worksheet_by_title('Sheet1')
    wks.set_dataframe(df,(1,1))


    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face recognition tutorial ',resized_img)
    if cv2.waitKey(10) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows

