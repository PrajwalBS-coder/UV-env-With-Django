from User.models import User

class UserSerializer():
    meta: User
    fields="__all__"