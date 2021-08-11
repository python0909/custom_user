from rest_framework.routers import DefaultRouter
from django.urls import path, include, re_path as url
from django.contrib.auth import views as auth_views
from Accounts.views import UseRegister ,UserProfile ,UpdateUserView,DeleteUserAdmin, DeleteUserManager ,AssignUserRole, UserLogin , ChangePasswordView , TempPassword , ForgotPassword


urlpatterns = [
    url(r'^register/$', UseRegister.as_view()),
    url(r'^profile/$', UserProfile.as_view()),
    url(r'^forgot_password/$', ForgotPassword.as_view()),
    url(r'^login/$', UserLogin.as_view()),
    url(r'^update/$', UpdateUserView.as_view()),
    path('delete_any/<int:pk>/', DeleteUserAdmin.as_view()),
    path('delete_user/<int:pk>/', DeleteUserManager.as_view()),
    path('role/<int:pk>/', AssignUserRole.as_view()),
    url(r'^set_pass/$', TempPassword.as_view()),
    url(r'^password/$', ChangePasswordView.as_view()),]
    