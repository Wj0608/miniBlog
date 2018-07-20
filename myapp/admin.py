from django.contrib import admin
from myapp.models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)



