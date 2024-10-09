from django.contrib.auth import login
from django.shortcuts import redirect

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User
from account.serializers import UserSerializer
from account.services.authentication.authentication import jwt_payload_handler, jwt_encode_handler, \
    CustomJWTAuthentication
from account.services.authentication.exceptions import *
from account.services.authentication.jwt import JSONWebTokenAPIView


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def admin_login(request):
    print(request.user)
    if request.user.is_authenticated:
        return redirect('admin/', permanent=True)

    token = request.GET.get('token', None)
    if not token:
        return redirect('/auth/', permanent=True)

    try:
        authentication = CustomJWTAuthentication()
        user, token = authentication.authenticate(token=token)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('admin/', permanent=True)
    except Exception as e:
        print(1111, e)
        return redirect('admin/login/', permanent=True)


class ProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):
        authentication = CustomJWTAuthentication()
        # user, token = authentication.authenticate(request=request)
        return Response(UserSerializer(request.user).data)


class AuthenticationAPIView(JSONWebTokenAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.get(username=serializer.validated_data['username'])
        except User.DoesNotExist:
            raise AuthenticationFailed('Неверный логин или пароль')

        if not user.check_password(serializer.validated_data['password']):
            raise AuthenticationFailed('Неверный логин или пароль')

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        try:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        except Exception:
            raise AuthenticationFailed('Ошибка авторизации пользователя')

        # payload['token'] = token
        response = self.serializer_class(user).data
        response['token'] = token

        return Response(response, status=status.HTTP_200_OK)


class RegistrationAPIView(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'success': True}, status=status.HTTP_200_OK)
