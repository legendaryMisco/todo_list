from django.urls import path
from . import views

urlpatterns = [
     path('register/', views.registerPage,name="register"),
     path('login/', views.loginPage,name="login"),
     path('logout/', views.logoutPage,name="logout"),

     path('account/', views.userAccount, name="account"),
     path('edit-account/', views.editAccount,name="edit-account"),
     path('delete-account/', views.deleteAccount,name="delete-account"),
     path('find-friends/', views.usersProfiles,name="find-friends"),
     path('user-profile/<str:pk>/', views.singleProfile,name="user-profile"),

 ]
