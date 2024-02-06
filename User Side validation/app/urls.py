from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.RegisterPage,name="registerPage"),
    path("register/",views.UserRegister,name="register"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("loginuser/",views.LoginUser,name="login"),
]