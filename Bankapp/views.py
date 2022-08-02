from django.shortcuts import render

from django.shortcuts import render, redirect
from Bankapp.models import Register, Createaccount, TrasactionDetails
import random
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
                        if Createaccount.objects.filter(email=email).exists():
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
        if Createaccount.objects.filter(email=email).exists():
            return HttpResponse("User Already Registered")
        if request.session['email'] == email:
            reg_user = Register.objects.get(email=email).id
            name = request.POST.get('name')
            gender = request.POST.get('gender')
            account_type = request.POST.get('account')
            initial_amount = request.POST.get('initial_amount')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            email = request.POST.get('email')
            account_no = random.randint(999999999, 9999999999)
            user = Createaccount.objects.create(Register_id=reg_user, name=name, email=email, gender=gender,
                                                account_type=account_type,
                                                initial_amount=initial_amount, phone=phone, address=address,
                                                account_no=account_no)
            return render(request, "bankindex.html", context={"user": user})
        else:
            return HttpResponse("Please Register 1st")
    return render(request, "create_account.html")


def bankindex(request):
    return render(request, "bankindex.html")



def transferMoney(request):
    email = request.session['email']
    account_detail = Createaccount.objects.get(email=email)
    account_no = account_detail.account_no
    closing_balance = TrasactionDetails.closing_balance
    name = account_detail.name
    context = {"account_no": account_no, "name": name, "closing_balance": closing_balance}
    if request.method == "POST":
        email = request.session['email']
        account_detail = Createaccount.objects.get(email=email)
        to_acc = request.POST.get('to_acc')
        print(to_acc)
        if Createaccount.objects.filter(account_no=to_acc).exists():
            debit_amount = request.POST.get('debit_amount')
            initial_amount = account_detail.initial_amount
            closing_balance = initial_amount - int(debit_amount)
            account_detail.initial_amount = closing_balance
            account_detail.save()
            user = TrasactionDetails.objects.create(acc_detail_id=account_detail.id, debit_amount=debit_amount,
                                                    closing_balance=closing_balance, to_acc=to_acc)
            rec_acc = Createaccount.objects.get(account_no=to_acc)
            rec_closing_balance = int(debit_amount) + rec_acc.initial_amount
            rec_acc.initial_amount = rec_closing_balance
            rec_acc.save()
            print(rec_acc)
            receiver_acc = TrasactionDetails.objects.create(acc_detail_id=rec_acc.id, credit_amount=debit_amount,
                                                            closing_balance=rec_closing_balance)
            context = {"user": user, "receiver_acc": receiver_acc}
            return render(request, "bankindex.html", context)
        else:
            return HttpResponse("Invalid Account number")
    return render(request, 'TransferMoney.html', context)


def deposite(request):
    email = request.session['email']
    account_detail = Createaccount.objects.get(email=email)
    account_no = account_detail.account_no
    name = account_detail.name
    context = {"account_no": account_no, "name": name}
    if request.method == "POST":
        email = request.session['email']
        account_detail = Createaccount.objects.get(email=email)
        credit_amount = request.POST.get('credit_amount')
        initial_amount = account_detail.initial_amount
        closing_balance = initial_amount + int(credit_amount)
        account_detail.initial_amount = closing_balance
        account_detail.save()
        user = TrasactionDetails.objects.create(acc_detail_id=account_detail.id, credit_amount=credit_amount,
                                                closing_balance=closing_balance)
        context = {"user": user}
        return render(request, "bankindex.html", context)
    return render(request, "Deposite.html", context)

def withdrawl(request):
    email = request.session['email']
    account_detail = Createaccount.objects.get(email=email)
    account_no = account_detail.account_no
    name = account_detail.name
    context = {"account_no": account_no, "name": name}
    if request.method == "POST":
        email = request.session['email']
        account_detail = Createaccount.objects.get(email=email)
        debit_amount = request.POST.get('debit_amount')
        initial_amount = account_detail.initial_amount
        closing_balance = initial_amount - int(debit_amount)
        account_detail.initial_amount = closing_balance
        account_detail.save()
        print(account_detail.initial_amount)
        user = TrasactionDetails.objects.create(acc_detail_id=account_detail.id, debit_amount=debit_amount,
                                                closing_balance=closing_balance)
        context = {"user": user}
        return render(request, "bankindex.html", context)
    return render(request, 'Withdrawl.html', context)


def transactionDetails(request):
    email = request.session['email']
    transaction_detail = TrasactionDetails.objects.filter(acc_detail__email=email)
    return render(request, 'TransectionDetails.html', {"transaction_detail": transaction_detail})

def balanceEnquiry(request):
    email = request.session['email']
    account_detail = Createaccount.objects.get(email=email)
    account_no = account_detail.account_no
    name = account_detail.name
    closing_balance = account_detail.initial_amount
    context = {"account_no": account_no, "name": name, "closing_balance": closing_balance}
    return render(request, "BalanceEnquiry .html", context)

def viewProfile(request):
    email = request.session['email']
    account_detail = TrasactionDetails.objects.filter(acc_detail__email=email).last()
    print(account_detail.closing_balance)
    return render(request, 'ViewProfile.html', {"account_detail": account_detail})

def adminprofile(request):
    account_detail = Createaccount.objects.all()
    transaction_detail = TrasactionDetails.objects.all()

    user = {"transaction_detail": transaction_detail, "account_detail": account_detail}
    return render(request, 'admindetail.html', user)


def logout(request):
    del request.session['email']
    return redirect("login")
