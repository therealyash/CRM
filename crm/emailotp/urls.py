from django.urls import path
from .views import request_otp_view, verify_otp_view

urlpatterns = [
    path('login/', request_otp_view, name='request-otp'),
    path('verify/', verify_otp_view, name='verify-otp'),
]
