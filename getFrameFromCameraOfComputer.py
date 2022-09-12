import cv2

cap = cv2.VideoCapture(0)

def getFrame(timeInterval):
    '''
    timeInterval：间隔时间，单位毫秒
    '''
    cv2.waitKey(timeInterval)
    flag, frame = cap.read()
    if(flag):
        return frame