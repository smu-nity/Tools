from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('agree/', views.agree, name='agree'),
    path('signup/', views.signup, name='signup'),
]
