from django.db import models


class Register(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.firstname


class Createaccount(models.Model):
    Register = models.OneToOneField(
        Register,
        on_delete=models.CASCADE, null=True, blank=True)
    GENDER_CHOICES = [('male', 'male'),
                      ('female', 'female'),
                      ('other', 'other')]

    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    account_type = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    initial_amount = models.IntegerField(default=1000)
    account_no = models.PositiveBigIntegerField(null=True, blank=True)
    rec_acc = models.PositiveBigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class TrasactionDetails(models.Model):
    acc_detail = models.ForeignKey(Createaccount, on_delete=models.CASCADE)
    debit_amount = models.IntegerField(blank=True, default=00)
    credit_amount = models.IntegerField(blank=True, default=00)
    to_acc = models.IntegerField(blank=True, null=True)
    closing_balance = models.IntegerField(blank=True, null=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=25)

    def __str__(self):
        return self.acc_detail.name
