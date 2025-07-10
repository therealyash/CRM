from django.urls import path
from .views import signup_view, profile_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
