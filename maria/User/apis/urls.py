from django.urls import path,include
from User.apis.get_all_users import get_all_users

urlpatterns = [
    path('users/',get_all_users,name='get_all_users'),
]