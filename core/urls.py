from django.urls import path
from .views import getHome
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("",getHome,name='home'),
    path('login/',LoginView.as_view(),name='login')
]
