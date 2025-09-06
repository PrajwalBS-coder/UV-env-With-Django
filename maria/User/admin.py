from django.contrib import admin

# Register your models here.
from User.Models.user import User
admin.site.register(User)