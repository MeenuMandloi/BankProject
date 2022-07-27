from django.db import models


class Register(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=8)

    def __str__(self):
        return self.firstname


class Create_account(models.Model):
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
    amount = models.IntegerField(default=1000)

    def __str__(self):
        return self.name
