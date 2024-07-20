from django.urls import path
from .views import RegistrationView, OTPView, OtpVerificationView

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('request-otp', OTPView.as_view(), name='request-otp'),
    path('verify-otp', OtpVerificationView.as_view(), name='verify-otp')
]