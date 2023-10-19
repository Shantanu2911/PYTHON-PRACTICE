# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 10:34:49 2022

@author: Shantanu Durgvanshi
"""
import smtplib

server = smtplib.SMTP('smtp.gmail.com',465)

server.starttls()

server.login("shantanudurgvanshi8@gmail.com","singh7579")

server.sendmail("shantanudurgvanshi8@gmail.com","vishaluprtou@gmail.com","Your book is really fantastic sir")
print("mail sent")