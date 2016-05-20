import mimetypes
import email
import email.mime.application
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import smtplib

# Create a text/plain message
msg = email.mime.Multipart.MIMEMultipart()
msg['Subject'] = 'topic'
msg['From'] = 'senderaddress@gmail.com'
msg['To'] = 'reciever@gmail.com'

# The main body is just another attachment
body = email.mime.Text.MIMEText("""Hello, how are you? """)
msg.attach(body)

# KML attachment
filename='abc.txt'
fp=open(filename,'rb')
att = email.mime.application.MIMEApplication(fp.read(),_subtype="txt")
fp.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)

s = smtplib.SMTP('smtp.gmail.com')
s.starttls()
s.login('senderaddress','password')
s.sendmail('senderaddress',['reciever@gmail.com'], msg.as_string())
s.quit()