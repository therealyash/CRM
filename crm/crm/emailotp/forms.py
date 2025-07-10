from django import forms
from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='Enter your email')

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6)


class VerifyOTPForm(forms.Form):
    otp = forms.CharField(label="Enter OTP", max_length=6)

