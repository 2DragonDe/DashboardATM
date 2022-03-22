from django.urls import path
from .views import login_view, register_user, profile
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/', profile, name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='users/change-password.html'), name='password_change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='users/password-change-done.html'), name='password_change_done'),
]