from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from . import models
from myapp.models import Register
# import mysql.container
# Create your views here.
def Index(request):
    return render(request,'myapp/index.html')
def register(request):
    return render(request, 'myapp/register.html')
def login(request):
    return render(request, 'myapp/login.html')
def succ(request):
    regobj = models.Register()

    name = request.POST.get('name')
    phone = request.POST.get('phone')
    mail = request.POST.get('mail')
    password = request.POST.get('password')
    confirmpassword = request.POST.get('confirmpassword')
    regobj.name = name
    regobj.mail = mail
    regobj.phone = phone
    regobj.password=password
    regobj.confirmpassword = confirmpassword
    regobj.save()
    return render(request, 'myapp/succ.html')

def done(request):
    regobj = models.Register()

    lmail = request.POST.get('lmail')
    lpassword = request.POST.get('lpassword')
    mail = regobj.mail
    password = regobj.password
    rs = Register.objects.all().filter(mail=lmail,password=lpassword)
    if rs:
        return HttpResponse("<h1> Ooops.....<h1>")

    else:
        return render(request, 'myapp/done.html')









# def succ(request):
#     # connected to the sqlite3
#     # db = mysqul.container.content()
#     db = sqlite3.connect('Registration')
#     # Created cursor from database registration
#     rs = db.cursor()
#     # created table name register and number is varchar
#     # rs.execute('''create table Register(name varchar(50), email varchar(100), phone varchar(10), passwd varchar(10))''')
#     # db.commit()
#     # add data in table
#     rs.execute(''' insert into Register values('Raja','@gmail.com','9099999999','raja1234#')''')
#     db.commit()
#     data = []
#     rs.execute('select * from Register')
#     for i in rs:
#         data.append(i)
#         print(i)
#
#     return render(request, 'myapp/succ.html', {'data':data})
