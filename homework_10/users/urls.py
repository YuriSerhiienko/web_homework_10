from django.urls import path
from .views import RegisterView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from django.views.generic import TemplateView

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "login/",
        LoginView.as_view(
            redirect_authenticated_user=False,
            template_name="users/login.html",
            authentication_form=LoginForm,
        ),
        name="login",
    ),
    path(
        "profile/",
        TemplateView.as_view(template_name="users/index.html"),
        name="profile",
    ),
    path(
        "logout/", LogoutView.as_view(template_name="users/logout.html"), name="logout"
    ),
]
