from django.urls import path
from . import views

urlpatterns = [
     path('direct-message/<str:pk>/', views.directMessage,name="direct-message"),
     # path('logout/', views.logoutPage,name="logout"),
]
