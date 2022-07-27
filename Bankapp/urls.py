from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register/', views.register, name="Register"),
    path('create_account/', views.create_account, name="create_account"),
    path('bankindex/', views.bankindex, name="bankindex"),
    path('TransferMoney/', views.TransferMoney, name="TransferMoney"),
    path('Withdrawl/', views.Withdrawl, name="Withdrawl"),
    path('BalanceEnquiry/', views.BalanceEnquiry, name="BalanceEnquiry"),
    path('ViewProfile/', views.ViewProfile, name="ViewProfile"),
    path('Deposite/', views.Deposite, name="Deposite"),
    path('TransectionDetails/', views.TransectionDetails, name="TransectionDetails"),

]
