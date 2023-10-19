import smtplib

server = smtplib.SMTP('smtp.gmail.com',25)

server.starttls()

server.login('shantanudurgvanshi8@gmail.com','singh7579')

server.sendmail("shantanudurgvanshi8@gmail.com","vishaluprtou@gmail.com","Your book is really fantastic sir")
print("mail sent")






















