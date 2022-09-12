from emailSender import send_mail
from getFrameFromCameraOfComputer import getFrame
import cv2
import mediapipe as mp
from multiprocessing import Process

class CFG:
    smtp_server = 'smtp.163.com'
    user = '***@163.com'    #163邮箱
    password = '***'   #开启163邮箱SMTP服务后得到的验证码
    receives = ['***@qq.com', '***@***'] #接收图片的邮箱，可以一次发送给多个邮箱
    interval = 1000 #获取图片的间隔时间，时间单位毫秒
    timeWait = 60*1000*1000 #发送图片后等待的时间
    face_mesh = mp.solutions.face_mesh.FaceMesh(
        static_image_mode=True,
        max_num_faces=1,
        min_detection_confidence=0.5
    )   #人脸识别器

def target1():
    while True:
        frame = cv2.cvtColor(getFrame(CFG.interval), cv2.COLOR_BGR2RGB)
        if CFG.face_mesh.process(frame).multi_face_landmarks:
            cv2.imwrite('person.jpg', frame)
            send_mail(CFG.smtp_server, CFG.user, CFG.password, CFG.receives)
            cv2.waitKey(CFG.timeWait)

def target2():
    cap = cv2.VideoCapture(0)
    while True:
        flag, frame = cap.read()
        if flag:
            cv2.imshow('0', frame)
        cv2.waitKey(CFG.interval)

if __name__ == '__main__':
    # Process(target=target1).start()
    # Process(target=target2).start()
    target1()