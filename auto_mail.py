import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("demoautoab@gmail.com","automation*123")
msg = 'hello, this is a test mail'

message = f"{msg}"
server.sendmail("demoautoab@gmail.com","studrijit@gmail.com",message)
