from django.urls import path

from auth.views import login_api_view, logout_api_view

app_name = "auth"

urlpatterns = [
    path("login/", login_api_view, name="login_api_view"),
    path("logout/", logout_api_view, name="logout_api_view")
]
