from django.urls import path
from users.views import register,login

urlpatterns=[
    path("users/register/",register,name="register"),
    path("users/login/",login,name="login"),
]