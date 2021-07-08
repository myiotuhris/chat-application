from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<str:room>/',views.room,name='room'),
    path('checkroom',views.checkRoom,name='checkRoom'),
    path('getmessage/<str:room>/',views.getMessages,name='getMessages'),
    path('send',views.sendMessage,name='sendMessage'),
]
