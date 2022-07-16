from django.urls import path
from . import views
urlpatterns  = [
    path('',views.Lists,name="lists"),
    path('todo-list/<str:pk>/',views.signleLists,name="list"),
    path('create-list/',views.addList,name="create-list"),
    path('update-list/<str:pk>/',views.updateList,name="update-list"),
    path('delete-list/<str:pk>/',views.deleteList,name="delete-list"),
    path('message-list/', views.messageList, name="message-list"),
]