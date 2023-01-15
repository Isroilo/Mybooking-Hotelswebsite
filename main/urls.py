from django.urls import path
from .views import *
urlpatterns = [
    path("hotels_all/", hotels_all_view),
    path("hotels/<int:pk>/", hotels_view),
    path("get_rooms/<int:pk>/", get_room_by_hotel),
    path("get_hotel/<int:pk>/", get_hotel),
    path("get_room/<int:pk>/", get_room),
    path("search_hotel_name/", search_hotel_name),
    path("hotel_order/<int:pk>/", hotel_order),
    path("filter_rooms_date/<int:pk>/", filter_rooms_date),
    path("filter_room_price/<int:pk>/", filter_room_price),
    path("search_rooms_date/<int:pk>/", search_rooms_date),
    path("create_comment/<int:pk>/", create_comment),
]