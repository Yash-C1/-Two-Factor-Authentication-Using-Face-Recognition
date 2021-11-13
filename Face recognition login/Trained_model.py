from os import name
import numpy as np
import cv2
from register import db
import register
import json
import streamlit as st

def trained_face_model(name_,pass_):
    training_data = []
    confidence_scores = []
    #gray_scale_training_data  = []

    face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
  
    my_col = db['Registered users']
    labels = []
    for x in my_col.find({'name' : name_,'password' : pass_}):
        arr = json.loads(x['photos'])
        np_arr = np.array(arr)
        np_arr = np_arr.astype(np.uint8)
        
        for j in range(100):
            training_data.append(np_arr[j])
            labels.append(j)

    if(len(training_data) == 0):
        return 0
    else:
        model = cv2.face.LBPHFaceRecognizer_create()
        model.train(np.asarray(training_data),np.asarray(labels))

        print("Model trained !")
    
        def sample_collector(img):    
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
            if faces is ():
                return None

            for (x,y,w,h) in faces:
                cropped_face = img[y:y+h, x:x+w]

            return cropped_face


        cap = cv2.VideoCapture(0)
        count = 0

        while True:

            ret, frame = cap.read()
            if sample_collector(frame) is not None:
                count += 1
                face = cv2.resize(sample_collector(frame), (200, 200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            #-----------------------------------------------------------
                results = model.predict(face)
            
                confidence = 100 * (1- (results[1]/400))

                confidence_scores.append(confidence)
            #-------------------------------------------------------------
                cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                cv2.imshow('Face', face)
         
            else:
                pass

            if cv2.waitKey(1) == 13 or count == 50: 
                break

        cap.release()
        cv2.destroyAllWindows() 


    #results = model.predict(samples)

        avg_confidence = sum(confidence_scores)/len(confidence_scores)

    # print(confidence_scores) 
    # print(avg_confidence)


        return avg_confidence







