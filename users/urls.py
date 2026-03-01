from tempfile import template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import UserRegisterView, logout_view
from .forms import UserLoginForm


urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="users/login.html", authentication_form=UserLoginForm
        ),
        name="login",
    ),
    path("logout/", views.logout_view, name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
]
