from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class VerifyUsername(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        if username is not None:
            username_exists = User.objects.filter(username=username).exists()
            if username_exists:
                response = {'username':[
                    'A User with this username already exists'
                ]}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                response = {'username': username}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'username': [
                    'This field is required'
                ]
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
