from django.urls import path

import auth.views

app_name = "auth"

urlpatterns = [
    # user create
    path(
        "create/", 
        auth.views.create_user_api_view, 
        name="create_user_api_view"
    ),
    
    # user login
    path(
        "login/", 
        auth.views.login_api_view, 
        name="login_api_view"
    ),
    
    # user logout
    path(
        "logout/", 
        auth.views.logout_api_view, 
        name="logout_api_view"
    )
]
