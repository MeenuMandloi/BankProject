from django.contrib import admin
from .models import Register, Createaccount, TrasactionDetails


class RegisterAdmin(admin.ModelAdmin):
    model = Register
    list_display = ("id", "firstname")


admin.site.register(Register, RegisterAdmin),
admin.site.register(Createaccount),
admin.site.register(TrasactionDetails),
