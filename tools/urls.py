from django.urls import path
from django.contrib.auth import views as auth_views
from .views import world_view, tools_home, register_user_view

app_name = "tools"

urlpatterns = [
    path("register/", register_user_view, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", tools_home, name="tools_home"),
    path("world/<int:world_id>/", world_view, name="world_view"),
]
