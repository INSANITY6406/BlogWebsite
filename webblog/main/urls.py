from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("signup",views.signUp,name="signup"),
    path("create_post",views.create_post,name="createpost"),
]
