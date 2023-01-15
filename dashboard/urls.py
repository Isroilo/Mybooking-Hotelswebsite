from django.urls import path
from .views import *
urlpatterns = [
    path("create_hotel/", create_hotel),
    path("create_room/", create_hotel),
]