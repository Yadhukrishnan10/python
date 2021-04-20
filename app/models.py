from django.db import models

# Create your models here.
from django.db import models
from common.fields import *


class Login(models.Model):
    username: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30,
                                                                                                 unique=True)
    password: Password(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
                                                                                                     max_length=8)
    type: Hidden() = models.CharField(max_length=5, default='U')


class User(models.Model):
    id: Hidden()
    log: Foreign(Login) = models.ForeignKey(Login, default=0, on_delete=models.CASCADE)
    name: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    profile: File(path='static/profile', preview={'width': 50, 'height': 50}, css='display:none',
                  start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='avatar.jpg',
                                                                                                max_length=30)
    email: Email(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',max_length=30)
    phone: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',max_length=30)
    address: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',max_length=30)


class Pharmacy(models.Model):
    id: Hidden()
    log: Foreign(model=Login, use={'type': 'P'}) = models.ForeignKey(Login, default=0, on_delete=models.CASCADE)
    name: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    phone: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)


class Staff(models.Model):
    id: Hidden()
    log: Foreign(model=Login, use={'type': 'S'}) = models.ForeignKey(Login, default=0, on_delete=models.CASCADE)
    name: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    phone: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    place: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30, default=0)
    email: Email(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
                                                                                               max_length=30)


class Product(models.Model):
    id: Hidden()
    # log: Foreign(model=Login,use={'type':'S'}) = models.ForeignKey(Login, default=0, on_delete=models.CASCADE)
    name: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    price: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    quantity: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
                                                                                                 max_length=30)
    profile: File(path='static/profile', preview={'width': 50, 'height': 50}, css='display:none',
                  start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='avatar.jpg',
                                                                                                max_length=30)


class Doctor(models.Model):
    id: Hidden()
    log: Foreign(model=Login, use={'type': 'D'}) = models.ForeignKey(Login, default=0, on_delete=models.CASCADE)
    name: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    section: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    phone: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    # lace: Text(start_wrap='<div class="form-group">', end_wrap='</div >')  = models.CharField( max_length=30,default=0)
    # email: Email(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',max_length=30)


class Bank(models.Model):
    # id:Hidden()
    # log: Foreign(Login) = models.ForeignKey(Login, default=0, on_delete=models.CASCADE)
    name: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    cardnumber: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    expmonth: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    expyear: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    cvv: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='', max_length=30)
    balance: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
                                                                                                max_length=30)
    customerid: Hidden(name="customerid_id") = models.ForeignKey(User, default=0, on_delete=models.CASCADE)


class Cart(models.Model):
    id: Hidden()
    quantity: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    price: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(max_length=30)
    productid: Hidden(name="productid_id") = models.ForeignKey(Product, default=0, on_delete=models.CASCADE)
    userid: Hidden(name="userid_id") = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    # status:Hidden() = models.CharField( max_length=5,default='pending')


class Transaction(models.Model):
    cartid: Hidden(name="productid_id") = models.ForeignKey(Cart, default=0, on_delete=models.CASCADE)
    customerid: Hidden(name="customerid_id") = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    amount: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
                                                                                               max_length=30)
    status: Hidden() = models.CharField(max_length=5, default='pending')


class Consult(models.Model):
    id: Hidden()
    doctorid: Hidden(name="doctorid_id") = models.ForeignKey(Doctor, default=0, on_delete=models.CASCADE)
    details: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
                                                                                                max_length=100)


class Appoinment(models.Model):
    id: Hidden()
    consultid: Hidden(name="consultid_id") = models.ForeignKey(Consult, default=0, on_delete=models.CASCADE)
    userid: Hidden(name="userid_id") = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    doctorid: Hidden(name="doctorid_id") = models.ForeignKey(Doctor, default=0, on_delete=models.CASCADE)


class Prescription(models.Model):
    id: Hidden()
    # userid: Hidden(name="userid_id") = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    prescription: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
                                                                                                max_length=30)
    doctorid: Hidden(name="doctorid_id") = models.ForeignKey(Doctor, default=0, on_delete=models.CASCADE)
    userid: Hidden(name="userid_id") = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    # user: Combo(options=User, start_wrap='<div class="form-group">', end_wrap='</div >') = models.ForeignKey(User,default='', max_length=30)

class Message(models.Model):
    id: Hidden()
    doctorid: Hidden(name="productid_id") = models.ForeignKey(Doctor, default=0, on_delete=models.CASCADE)
    userid: Hidden(name="customerid_id") = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    message: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
                                                                                               max_length=30)
    type: Hidden() = models.CharField(max_length=5, default='')



#
# class Message(models.Model):
#     id: Hidden()
#     doctorid: Hidden(name="doctorid_id") = models.ForeignKey(Doctor, default=0, on_delete=models.CASCADE)
#     userid: Hidden(name="doctorid_id") = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
#     message: Text(start_wrap='<div class="form-group">', end_wrap='</div >') = models.CharField(default='',
