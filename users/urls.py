from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.RegistrationView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login'),
    path('users_list/', views.UsersListView.as_view()),
]
