from django.urls import path
from django.contrib.auth import views as auth_views
from account import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
