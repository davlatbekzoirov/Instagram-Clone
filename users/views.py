from rest_framework.generics import CreateAPIView
from .serializers import UserSignUpSerializer
from .models import User
from rest_framework import permissions

class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny, )
    serializer_class = UserSignUpSerializer