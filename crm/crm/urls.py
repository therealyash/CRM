from django.contrib import admin
from django.urls import path, include
from dashboard.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Homepage

    path('lead/', include('lead.urls')),
    path('campaign/', include('campaign.urls')),
    path('automation/', include('automation.urls')),
    path('dashboard/', include('dashboard.urls')),

    # ✅ Auth routes — base login/logout/password
    path('accounts/', include('django.contrib.auth.urls')),

    # ✅ User management — signup, profile
    path('users/', include('users.urls')),

    # ✅ OTP login — from custom auth app
    path('otp/', include('emailotp.urls')),
]
