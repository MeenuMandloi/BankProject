from django.shortcuts import render

from django.shortcuts import render, redirect
from Bankapp.models import Register, Create_account
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.urls import reverse


def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if Register.objects.filter(email=email).exists():
            return HttpResponse("User Already Registered")
        else:
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            password = request.POST.get('password')
            repassword = request.POST.get('repassword')

            user = Register.objects.create(firstname=firstname, lastname=lastname,
                                           phone=phone, email=email, password=password)
            if user:
                if password != repassword:
                    return HttpResponse("Password does not match")
                else:
                    return render(request, "index.html", context={"user": user})
    else:
        return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        super_user = User.objects.filter(email=email)
        user = authenticate(request, email=email, password=password)
        check_user = Register.objects.filter(email=email)
        if check_user:
            for data in check_user:
                if data.email == email:
                    if data.password == password:
                        request.session['email'] = email
                        user = Register.objects.get(email=email)
                        context = {'user': user}
                        if Create_account.objects.filter(email=email).exists():
                            return render(request, "bankindex.html", context)
                        else:
                            return render(request, "create_account.html", context)
                    else:
                        return HttpResponse('Please enter valid Password.')
                else:
                    return HttpResponse('Please enter valid email.')

    return render(request, 'index.html')


def create_account(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if Create_account.objects.filter(email=email).exists():
            return HttpResponse("User Already Registered")
        if request.session['email'] == email:
            name = request.POST.get('name')
            email = request.POST.get('email')
            gender = request.POST.get('gender')
            account_type = request.POST.get('account')
            amount = request.POST.get('amount')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            email = request.POST.get('email')
            user = Create_account.objects.create(name=name, email=email, gender=gender, account_type=account_type,
                                                 amount=amount, phone=phone, address=address)
            return render(request, "bankindex.html", context={"user": user})
        else:
            return HttpResponse("Please Register 1st")
    return render(request, "create_account.html")


def bankindex(request):
    return render(request, "bankindex.html")


def TransferMoney(request):
    return render(request, 'TransferMoney.html')


def Deposite(request):
    return render(request, 'Deposite.html')


def Withdrawl(request):
    return render(request, 'Withdrawl.html')


def TransectionDetails(request):
    return render(request, 'TransectionDetails.html')


def BalanceEnquiry(request):
    return render(request, 'BalanceEnquiry .html')


def ViewProfile(request):
    return render(request, 'ViewProfile.html')
