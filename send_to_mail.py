import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

fromaddr = "den.shell.00@mail.ru"
toaddr = "den.shell.00@mail.ru"
mypass = "a8PN2cPi07bw8FHN6Lpg"
reportname = "log.txt"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Привет от питона"
text = "Hello"
msg.attach(MIMEText(text))

with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = f'attachment; filename="{basename(reportname)}"'
    msg.attach(part)

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()