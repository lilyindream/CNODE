from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from src.library.getPath import getCasePath,getReportPath
from src.library.publicMethod import formatdate
from email.header import Header
import smtplib
import  unittest
import time,os

#*************************定义发送邮件
def send_mail(file_new):
    f=open(file_new,'rb')
    mail_body=f.read()
    f.close()

    sender='aquarius90123@126.com'
    receiver='928912906@qq.com'
    subject="Python自动化测试报告"
    username='aquarius90123@126.com'
    password='lily123456'


    msg=MIMEText(mail_body,'html','utf-8')
    msg['Subject']=Header(subject,'utf-8')
    msg['From']='lily<aquarius90123@126.com>'
    msg['to']='928912906@qq.com'

    smtp=smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print("mail has sent out")


  #************查找到测试报告目录，找到哦啊最新生成的测试报告文件
def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+"\\" + fn))
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    filename=os.path.join(getReportPath(),formatdate()+'result.html')
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,
                          title='Cnode社区自动化测试报告',
                          description='环境:win7 浏览器:chrome')
    discover=unittest.defaultTestLoader.discover(getCasePath(),pattern='*_cases.py')
    runner.run(discover)
    fp.close()
    file_path=new_report(getReportPath())
    send_mail(file_path)