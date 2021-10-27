'''
Description: 
Author: [cdy]
Date: 2021-09-30 19:20:01
LastEditors: [cdy]
LastEditTime: 2021-09-30 22:29:32
'''
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import requests
import time

headers = {
    'Referer': 'https://teaching.applysquare.com/S/Index/index.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}
post_url = "https://teaching.applysquare.com/Api/User/ajaxLogin"
pwd = {'email': '18252035002',
       'password': '771b53e80d5397ec63657cb701f650f3'}
# data = {
#     'p': 1,
# 'select': 0,
# 'plan_id': -1,
# 'uid': 218318,
# 'cid': 20147,
# }
# 设置邮箱

# 发送邮箱的账号密码
username = "luckycdy@163.com"
password = "8488123cdy,"
# 邮箱的发送头，如有没有昵称等
sender = "luckycdy@163.com"
# 接收邮箱
receiver = ["yuyadong@outlook.com"]


def send_email(mainbody):
    smtp = smtplib.SMTP()
    # 发送邮箱的 SMTP 服务器
    smtp.connect('smtp.163.com', 25)
    smtp.login(username, password)
    message = MIMEText(mainbody, 'plain', 'utf-8')
    message['From'] = "luckycdy <luckycdy@163.com>"
    message['To'] = "yuyadong@outlook.com"
    subject = "出现新帖子"
    message['Subject'] = Header(subject, 'utf-8')
    smtp.sendmail(sender, receiver, message.as_string())
    smtp.quit()


s = requests.session()
r = s.post(post_url, headers=headers, data=pwd)
token = r.json()["message"]["token"]
info_url = f"https://teaching.applysquare.com/Api/Discuss/getCourseCardList/token/{token}?p=1&select=0&plan_id=-1&uid=218318&cid=20147"
count = 0
t = 0
while count <= 2:
    t += 1
    r2 = s.get(info_url, headers=headers)
    count = len(r2.json()["message"]["list"])
    time.sleep(60)
    print(f'已监测 {t} min')
send_email('出现新帖子')
print(r2.json())
