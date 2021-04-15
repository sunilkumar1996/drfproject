from django.urls import include, path

from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path("change-password/", views.ChangePasswordSerializer, name="change-pasowrd"),
    # path('auth/register/', views.registeruser, name="register"),
]