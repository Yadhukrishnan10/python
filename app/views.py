from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from common import __views
from app.models import *
from pharmacy_prj.settings import STASTIC_FOLDER
import os


def index(request):
    login = Login.objects.filter(username='admin', password='admin').first()
    if login is None:
        login = Login(username='admin', password='admin', type='A').save();
        login = Login.objects.filter(username='admin', password='admin').first()
        User(log=login, name='Admin', email='admin').save();
    return __views.__form(request, 'User', 'index')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        login = Login.objects.filter(username=username, password=password).first()

        delete_session(request)
        if login is not None:

            # request.session['profile'] = user.profile;
            request.session['log_id'] = login.id;

            request.session['role'] = login.type;
    datas = User.objects.all()
    page = 'index.html'
    if login is None:
        return render(request, page, {'model': datas})
    elif login.type is 'A':
        page = 'admin/admin_home.html'
    elif login.type is 'U':
        user = User.objects.filter(log=login).first()
        request.session['name'] = user.name;
        request.session['user_id'] = user.id;
        page = 'user/user_home.html'
    elif login.type is 'P':
        user=Pharmacy.objects.filter(log=login).first()
        request.session['name']=user.name;
        request.session['user_id']=user.id;
        page = 'pharmacy/pharmacy_home.html'
    elif login.type is 'S':
        user=Staff.objects.filter(log=login).first()
        request.session['name']=user.name;
        request.session['user_id']=user.id;
        page = 'staff/staff_home.html'
    elif login.type is 'D':
        user=Doctor.objects.filter(log=login).first()
        request.session['name']=user.name;
        request.session['user_id']=user.id;
        page = 'doctor/doctor_home.html'

    return render(request, page, {'model': datas})


def delete_session(request):
    try:
        del request.session['name']
        del request.session['profile']
        del request.session['log_id']
        del request.session['user_id']
        del request.session['role']
    except  KeyError:
        pass

def logout(request):
    delete_session(request)
    return render(request, 'index.html')

def pharmacy_products(request):
    objs=Product.objects.all()
    return render(request, 'pharmacy/pharmacy_products.html',{'objs':objs})

def products(request):
    objs=Product.objects.all()
    return render(request, 'admin/products.html',{'objs':objs})

def view_products(request):
    objs=Product.objects.all()
    return render(request, 'user/view_products.html',{'objs':objs})


def cart(request):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        cid = request.POST.get('userid')
        pid = request.POST.get('productid')

        cart = Cart.objects.filter(productid_id=pid).first()
        if cart is None:
            price = float(quantity) * float(price)
            Cart(quantity=quantity, price=price, userid_id=cid, productid_id=pid).save()

        else:
            cart.price = float(quantity) * float(cart.price)
            cart.quantity = int(quantity) + int(cart.quantity)
            cart.save()
        datas = Product.objects.all()
        cart = Cart.objects.filter(userid_id=cid).first()
        return render(request, 'user/viewproducts.html', {'model': datas, 'carts': cart})


def transactions(request):
    msg = "transaction failed"
    if request.method == "POST":
        name = request.POST.get('name')
        cardnumber = request.POST.get('cardnumber')
        cvv = request.POST.get('cvv')
        expmonth = request.POST.get('expmonth')
        expyear = request.POST.get('expyear')
        tot = request.POST.get("subtotal")

        # cid = request.POST.getlist('cartid')
        # cusid = request.POST.get("customerid")
        cid = request.POST.getlist('cartid')
        for i in cid:
            crt = Cart.objects.filter(id=i).first()
            Transaction()
            print(crt)
        cusid = request.POST.get("customerid")


        bank = Bank.objects.filter(name=name, cardnumber=cardnumber, cvv=cvv, expmonth=expmonth,
                                   expyear=expyear).first()
        if bank is None:
            return __views.render(request, 'user/error.html',
                                  {'cid': cid, 'cusid': cusid, 'msg': "payment failed"})
        else:
            print(tot)
            bank.balance = float(bank.balance) - float(tot)
            bank.save()
            for i in cid:
             Transaction(amount=tot, customerid_id=cusid, cartid_id=i).save()
            Transaction(amount=tot)
             # Transaction(amount=tot, customerid_id=cusid, cartid_id=i).save()
            msg = "payment sucessful"
    else:
        cid = request.GET.getlist("cartid")
        cusid = request.GET.get("customerid")
        msg = ""

    return render(request, 'user/payment.html', {'cid': cid, 'cusid': cusid})


def payment(request):
    if request.method == 'POST':
        print("test list")
    cid = request.POST.getlist('cartid')
    cusid = request.POST.get("customerid")
    tot = request.POST.get("subtotal")
    print(tot)


    return render(request, 'user/payment.html', {'cid': cid, 'cusid': cusid, 'tot': tot})


def deletecart(request,id):
    dlt = Cart.objects.get(pk=id)
    dlt.delete()
    return __views.back(request)

def addconsulting(request):
    if request.method == "POST":
        details = request.POST.get('details')
        did = request.POST.get("doctorid")
        Consult(details=details, doctorid_id=did).save()
    return __views.back(request)

def appoinment(request):

    if request.method == "POST":
        cid = request.POST.get("consultid")
        uid = request.POST.get("userid")
        did = request.POST.get("doctorid")
        print(cid,uid,did)
        Appoinment(consultid_id = cid, userid_id = uid, doctorid_id = did).save()
    return __views.back(request)

def prescription(request):
    if request.method == "POST":
        uid = request.POST.get("userid")
        did = request.POST.get("doctorid")
        pres = request.POST.get("prescription")
        print(pres, uid, did)
        Prescription(prescription = pres, userid_id=uid, doctorid_id=did).save()
    return __views.back(request)

def message(request):
    if request.method == "POST":
        msg = request.POST.get('message')
        did = request.POST.get("doctorid")
        uid = request.POST.get("userid")
        ty = request.POST.get("type")

        Message(message=msg, doctorid_id=did, userid_id=uid , type= ty).save()

    return __views.back(request)
def error(request):
    return (render,'user/error.html')


