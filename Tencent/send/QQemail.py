import smtplib
from time import sleep
from email.mime.text import MIMEText

#_user = ""
#_pwd = ""
#_to = ""

_waite = 5#min

_user = str(input("User : "))
_pwd = str(input("Pwd : "))
_to = str(input("To : "))
_subject = str(input("Subject : "))
msg = MIMEText(str(input("Content : ")))
_quantity = int(input("Quantity : "))

#msg = MIMEText("Test")
msg["Subject"] = _subject
msg["From"] = _user
msg["To"] = _to

print("Loading...")

for i in range(_quantity):
 try:
  print(str(i + 1) + " : ", end="")
  s = smtplib.SMTP_SSL("smtp.qq.com", 465)
  s.login(_user, _pwd)
  s.sendmail(_user, _to, msg.as_string())
  s.quit()
  print ("Success!")
  sleep(0.5)
 except smtplib.SMTPException:
  print ("Error !")
  i = i-1
  for n in range(_waite*60):
    print("Please Waite " + str(_waite) + " min...")
    print("Waited : " + str(n+1) +" s")
    sleep(1)
