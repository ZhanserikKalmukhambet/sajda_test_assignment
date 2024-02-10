from django.urls import path
from .views import SignUpView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', TokenObtainPairView.as_view(), name='sign-in'),
    path('access/', TokenRefreshView.as_view(), name='refresh')
]