from django.urls import path
from . import views
urlpatterns = [
      path('', views.home, name='home'),
      path('signup', views.handleSignUp, name="handleSignUp"),
      path('login', views.handleLogin, name="handleLogin"),
      path("logout", views.handleLogout, name="handleLogout"),

]