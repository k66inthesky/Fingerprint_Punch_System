import smtplib
from email.mime.text import MIMEText
from datetime import datetime as dt
import pandas as pd
import numpy as np


#Read txt
f = open("employee_punch_record.txt", "r")
r=f.read()
LINE_NUM=int(len(r)/34) #34 words per line.
l_txt_employee=[]
for i in range(LINE_NUM):
    l_txt_employee.append(r[10+34*i])

#Find who was absent today.
employee_ammount = 5 #the ammount of employees
l_absent,l_employee=[],[]
tmp=np.linspace(1,employee_ammount,employee_ammount)
l_employee.append(0)
for i in range(len(tmp)):
    l_employee.append(int(tmp[i]))
NOONE_ABSENT=True

for i in range(LINE_NUM):
    l_employee[int(l_txt_employee[i])]=999 #means the employee punched.
for i in range(1,employee_ammount+1):#cuz our fingerprint is from 1 to 127.
    if l_employee[i]!=999: #if the employee didn't punch.
        l_absent.append(i)
        NOONE_ABSENT=False
        
#Read employee_table.csv
employee_table=pd.read_csv('employee_table.csv')
l_employee_table=employee_table['Name']


#sender id and passward
gmail_user = "xxx" #sender mail id
gmail_passwd = "xxx"#sender mail password

str_messege=''
if NOONE_ABSENT == True:
    messege=str(dt.now())+' \nNobody was absent today.'
    str_messege+=messege
else:
    for i in range(len(l_absent)):
        messege=str(dt.now())+' \nEmployee ' + str(l_employee_table[l_absent[i]]) + ' was absent today.\n'
        str_messege+=messege
msg = MIMEText(str_messege)#context
msg['Subject'] = '[System Mail]Employee Absent'#title
msg['From'] = gmail_user
msg['To'] = 'xxx' #reciever, can be manager or teacher.

server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.ehlo()
server.login(gmail_user,gmail_passwd)
server.sendmail(msg['From'],msg['To'],msg.as_string())
server.quit()


print('Email End')
