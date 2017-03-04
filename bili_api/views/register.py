from rest_framework.generics import (CreateAPIView)
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from ..serializers.register import RegisterSerializer

class RegisterListView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
