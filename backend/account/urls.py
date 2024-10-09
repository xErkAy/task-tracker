from django.urls import re_path as path
from account.authentication import AuthenticationAPIView, RegistrationAPIView, ProfileAPIView

urlpatterns = [
    path('auth/$', AuthenticationAPIView.as_view(), name='user-login'),
    path('auth/sign-up/$', RegistrationAPIView.as_view(), name='user-sign-up'),
    path('profile/$', ProfileAPIView.as_view(), name='profile'),
]