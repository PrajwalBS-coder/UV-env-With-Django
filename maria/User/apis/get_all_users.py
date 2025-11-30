from rest_framework.response import Response
from rest_framework.decorators import api_view
from User.Models.user import User
from User.serializers import UserSerializer

@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)