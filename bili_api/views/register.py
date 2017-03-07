from rest_framework.generics import (CreateAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

from ..serializers.register import RegisterSerializer


class RegisterListView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data['email']
            if User.objects.filter(email=email).exists():
                response = {
                    'email': [
                        'A User with that email already exists'
                    ]
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            username = serializer.data['username']
            print(username)
            user = User.objects.get(username=username)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            content = {
                'username': username,
                'token': token
            }
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
