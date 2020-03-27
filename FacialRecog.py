import cv2
import numpy as np

#  output:
def request_video_stream():
    capture_obj = cv2.VideoCapture(0)
    
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter('help.avi',fourcc, 30.0, (int(capture_obj.get(3)),int(capture_obj.get(4)))) # create a video writer for saving 
    
    while(capture_obj.isOpened()):
        ret,frame = capture_obj.read()
        # any operations on it here
        if(ret == True):
            out.write(frame)    # save video stream
        
            cv2.imshow('frame',frame)
            if(cv2.waitKey(1))& 0xFF == 27:
                break
        else:
            break
        
    capture_obj.release()
    out.release()
    cv2.destroyAllWindows() # release
    return 0


request_video_stream()
# Idea is to detect a face, take three pictures of the peculiar face.
