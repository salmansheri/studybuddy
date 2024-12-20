from django.urls import path


from . import views 

urlpatterns = [
    path("auth/", views.sign_in, name="auth"), 
    path("", views.home, name='home'),
    path("room/<str:pk>", views.room, name="room"), 
    path("create-room/", views.createRoom, name="create-room"), 
    path("update-room/<str:pk>", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>", views.deleteroom, name="update-room"),
]
