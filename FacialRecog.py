import cv2
import numpy as np
import tensorflow as tf

#  output:
def request_video_stream():
    capture_obj = cv2.VideoCapture(0)
    
    
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter('help.avi',fourcc, 30.0, (int(capture_obj.get(3)),int(capture_obj.get(4)))) # create a video writer for saving 
    
    while(capture_obj.isOpened()):
        ret,frame = capture_obj.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # any operations on it here
        if(ret == True):
            
            out.write(frame)    # save video stream
            
            
            #cv2.imshow('frame',gray)
            break_ret =detect_face(gray)
            if break_ret==False :
                break
        else:
            break
        
    capture_obj.release()
    out.release()
    cv2.destroyAllWindows() # release
    return 0


request_video_stream()


def detect_face(frame):
    face_cascade = cv2.CascadeClassifier('D:\\Opecv\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow('frame',frame)
    if(cv2.waitKey(1))& 0xFF == 27:
                return False
    return True


# Just to see if frames are being sent.
def counter(i,frame):
    result = frame.transpose(2,0,1).reshape(3,-1)
    print(result)
    print(i)
    i=i+1
    return i
    
# Idea is to detect a face, take three pictures of the peculiar face. --> use open cv to get those faces 
    

# using tensorflows object detection API I will route this to a function using the API

# As the opencv already outputs video as a numpy array, we will use that to convert 



"""
https://www.pyimagesearch.com/2017/09/11/object-detection-with-deep-learning-and-opencv/
"""
