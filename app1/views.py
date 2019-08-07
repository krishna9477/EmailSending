from django.shortcuts import render

# Create your views here.

import smtplib
content="hello Welcome to Ismail Basha"
server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('vamsi9477@gmail.com','vamsi66@V')
server.sendmail('vamsi9477@gmail.com','skismail094@yahoo.com',content)
server.quit()


def showindex(request):
    return render(request,"index.html")