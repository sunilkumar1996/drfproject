from django.urls import include, path
from rest_auth.views import PasswordResetConfirmView, PasswordResetView
from . import views

urlpatterns = [
    path('users/', include('users.urls')),
    path('auth/', include('rest_auth.urls')),
    path("auth/password/reset/", PasswordResetView.as_view(), name="rest_password_reset",),
    path("auth/password/reset/confirm/", PasswordResetConfirmView.as_view(), name="rest_password_reset_confirm"),
    # path('rest-auth/', include('rest_framework.urls')),
    # path('auth/registration/', include('rest_auth.registration.urls')),
    path("home/", views.example_view),
]