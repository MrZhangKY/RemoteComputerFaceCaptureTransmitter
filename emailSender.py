import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_mail(smtp_server, user, password, receives):

    '''
    smtp_server：发送邮箱服务器（smtp.163.com）
        smtp_server = 'smtp.163.com'
    user：'发送邮箱用户名'
        user = '用户名'
    password：'发送邮箱密码'
        password = '密码'
    receives：接受邮箱列表
        receives = ['你需要发给的邮箱1','你需要发给的邮箱2','你需要发给的邮箱3'...]
    '''

    # 发送邮件和主题内容
    subject = '远程电脑异常警告！！！'
    content = '<html><h1 style="color:red">远程电脑有人接近！！！</h1></html>'

    # 构建发送与接收信息
    msg_root = MIMEMultipart()
    msg_root.attach(MIMEText(content, 'html', 'utf-8'))
    msg_root['subject'] = subject
    msg_root['From'] = user
    msg_root['To'] = ','.join(receives)

    # 构造附件3（附件为img）
    att3 = MIMEImage(open('person.jpg', 'rb').read())
    att3["Content-Type"] = 'application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename="person.jpg"'
    msg_root.attach(att3)

    # SSL协议端口号要使用465
    smtp = smtplib.SMTP_SSL(smtp_server, 465)

    # H E L O 向服务器标识用户身份
    smtp.helo(smtp_server)
    # 服务器返回结果确认
    smtp.ehlo(smtp_server)
    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)

    print("Start send email...")

    smtp.sendmail(user, receives, msg_root.as_string())

    smtp.quit()
    print("Send End！")
    print('============================================================================================')
