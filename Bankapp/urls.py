from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register/', views.register, name="Register"),
    path('create_account/', views.create_account, name="create_account"),
    path('bankindex/', views.bankindex, name="bankindex"),
    path('TransferMoney/', views.transferMoney, name="transferMoney"),
    path('Withdrawl/', views.withdrawl, name="withdrawl"),
    path('BalanceEnquiry/', views.balanceEnquiry, name="balanceEnquiry"),
    path('ViewProfile/', views.viewProfile, name="viewProfile"),
    path('Deposite/', views.deposite, name="deposite"),
    path('TransectionDetails/', views.transactionDetails, name="transectionDetails"),
    path('logout/', views.logout, name="logout"),
    path('adminprofile/', views.adminprofile, name="adminprofile"),

]
