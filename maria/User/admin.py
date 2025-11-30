from django.contrib import admin

# Register your models here.
from User.Models.user import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=[
        'username',
        'email',
        'first_name',
        'last_name',
        'date_joined'
    ]
    list_filter=[
        'email'
    ]