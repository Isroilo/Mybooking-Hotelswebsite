from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Photo
        fields = "__all__"


class Hotel_orderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Hotel_order
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Room
        fields = "__all__"


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Advantages
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Region
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"





