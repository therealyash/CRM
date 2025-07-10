from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import login
from .models import EmailOTP
from .forms import EmailForm, OTPForm
import random
from django.views.decorators.cache import never_cache

@never_cache
def request_otp_view(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        print("POST received")  # ✅ Debug line

        if form.is_valid():
            email = form.cleaned_data['email']
            print(f"Form valid, email: {email}")  # ✅ Debug line

            user = User.objects.filter(email=email).first()
            if not user:
                messages.error(request, "No user with this email.")
                return redirect('request-otp')

            otp = str(random.randint(100000, 999999))
            EmailOTP.objects.create(user=user, otp=otp)

            send_mail(
                subject='Your OTP Code',
                message=f'Your OTP is: {otp}',
                from_email='your@email.com',
                recipient_list=[email],
                fail_silently=False,
            )

            request.session['otp_user_id'] = user.id
            return redirect('verify-otp')

        else:
            print("Form not valid")  # ✅ Debug
            print(form.errors)      # ✅ See exact problem in console

    else:
        form = EmailForm()

    return render(request, 'emailotp/request_otp.html', {'form': form})



from .forms import VerifyOTPForm

@never_cache
def verify_otp_view(request):
    if 'otp_user_id' not in request.session:
        messages.error(request, "Session expired or invalid access.")
        return redirect('request_otp')

    if request.method == 'POST':
        form = VerifyOTPForm(request.POST)
        if form.is_valid():
            user_id = request.session['otp_user_id']
            otp = form.cleaned_data['otp']
            try:
                otp_record = EmailOTP.objects.get(user_id=user_id, otp=otp)
                login(request, otp_record.user)
                request.session.pop('otp_user_id', None)  # ✅ safe delete
                messages.success(request, "Login successful!")
                return redirect('dashboard')
            except EmailOTP.DoesNotExist:
                messages.error(request, "Invalid OTP.")
    else:
        form = VerifyOTPForm()

    return render(request, 'emailotp/verify_otp.html', {'form': form})

