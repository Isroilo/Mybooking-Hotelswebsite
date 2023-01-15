from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import *
from main.serializer import *
from main.serializer import *
from main.models import *


@api_view(['POST'])
def create_hotel(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    map_lot = request.POST.get('map_lot')
    map_long = request.POST.get('map_long')
    region = request.POST.get('region')
    rating = request.POST.get('rating')
    advantages = request.POST.getlist('advantages')
    photo = request.FILES.getlist("photo")
    description = request.POST.get("description")
    center = request.POST.get("center")
    new_hotel =  Hotel.objects.create(
            user = request.user,
            name=name,
            map_lot=map_lot,
            map_long=map_long,
            region_id=region,
            rating=rating,
            description=description,
            center=center,
            )
    try:
            for p in photo:
                img = Newsphoto.objects.create(
                        img=p
                    )
                new_hotel.photo.add(img)
                new_hotel.save()
    except:
        pass
    try:
            for x in advantages:
                advantage=Advantages.objects.create(
                    advantage = x
                )
                new_hotel.advantages.add(advantage)
                new_hotel.save()
    except:
        pass
    return Response({"message":"create success"})


@api_view(['POST'])
def create_room(request):
    number = request.POST.get('number')
    price = request.POST.get('price')
    hotel = request.POST.get('hotel')
    in_slider = request.POST.get('in_slider')
    advantages = request.POST.getlist('advantages')
    is_active = request.POST.get('is_active')
    photo = request.FILES.getlist("photo")
    room_type = request.POST.get("room_type")
    description = request.POST.get("description")
    new_room =  Restoran.objects.create(
            number=number,
            price=price,
            hotel=hotel,
            in_slider=in_slider,
            is_active=is_active,
            room_type=room_type,
            description=description,
            )
    try:
            for img in photo:
                photo = Newsphoto.objects.create(
                        photo=img
                    )
                new_room.photo.add(photo)
                new_room.save()
    except:
        pass
    try:
            for x in advantages:
                advantages=Advantages.objects.create(
                    advantages = i
                )
                new_room.advantages.add(advantages)
                new_room.save()
    except:
        pass
    return Response({"message":"create success"})