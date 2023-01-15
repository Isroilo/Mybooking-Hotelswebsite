from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import *
from .serializer import *

@api_view(['GET'])
def hotels_all_view(request):
    hotels = Hotel.objects.all().order_by('-id')
    ser = HotelSerializer(hotels, many=True)
    return Response(ser.data)


@api_view(['GET'])
def hotels_view(request,pk):
    region = Region.objects.get(pk=pk)
    hotels = Hotel.objects.filter(region=region)
    ser = HotelSerializer(hotels, many=True)
    return Response(ser.data)


@api_view(['GET'])
def get_hotel(request,pk):
    hotel = Hotel.objects.get(pk=pk)
    ser = HotelSerializer(hotel)
    return Response(ser.data)


@api_view(['GET'])
def get_room(request,pk):
    room = Room.objects.get(pk=pk)
    ser = RoomSerializer(room)
    return Response(ser.data)


@api_view(['GET'])
def get_room_by_hotel(request,pk):
    hotel = Hotel.objects.get(id=pk)
    rooms = Room.objects.filter(hotel=hotel).order_by('-id')
    ser = RoomSerializer(rooms, many=True)
    return Response(ser.data)


@api_view(['POST'])
def search_hotel_name(request):
    name = request.POST.get("name")
    hotels = Hotel.objects.filter(name__icontains=name)
    ser = HotelSerializer(hotels, many=True)
    return Response(ser.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def hotel_order(request,pk):
    phone = request.POST.get('phone')
    pas_photo = request.FILES.get('pas_photo')
    f_name = request.POST.get('f_name')
    l_name = request.POST.get('l_name')
    room = request.POST.get('room')
    email = request.POST.get("email")
    start = request.POST.get('start')
    end = request.POST.get("end")
    start_date = start.replace('-', '')
    end_date = end.replace('-', '')
    hotel_room= Room.objects.get(pk=pk)
    hotel_orders = hotel_room.room_order.all()
    busy_rooms = []
    for d in range(int(start_date), int(end_date) + 1):
        busy_rooms.append(d)
    if hotel_orders:
        for hotel_order in hotel_orders:
            ds = str(hotel_order.start).replace('-', '')
            de = str(hotel_order.end).replace('-', '')
            for i in range(int(ds), int(de) + 1):
                if i in busy_rooms:
                    hotel_room.status = 2
    if hotel_room.status == 1:
        new_order = Hotel_order.objects.create(
            user=request.user,
            pas_photo=pas_photo,
            f_name=f_name,
            l_name=l_name,
            start=start,
            end=end,
            room_id=room,
            email=email,
        )
        return Response({"message": "create success"})
    return Response({"message": "bu kunlarga bu xona band iltimos boshqa xona tanlang"})


@api_view(['POST'])
def filter_rooms_date(request,pk):
    date_start = request.POST.get('start').replace('-', '')
    date_end = request.POST.get('end').replace('-', '')
    hotel = Hotel.objects.get(pk=pk)
    rooms = Room.objects.filter(hotel=hotel)
    free_rooms = []
    for room in rooms:
        hotel_orders = room.room_order.all()
        dates = []
        xx = True
        for d in range(int(date_start), int(date_end)+1):
            dates.append(d)
        if hotel_orders:
            for hotel_order in hotel_orders:
                ds = str(hotel_order.start).replace('-', '')
                de = str(hotel_order.end).replace('-', '')
                for i in range(int(ds), int(de)+1):
                    if i in dates:
                        xx = False
        if xx == True:
            free_rooms.append(room)
    if len(free_rooms) > 0:
        ser = RoomSerializer(free_rooms, many=True)
        return Response(ser.data)
    else:
        return Response({"message": "bu kunlarga bosh xonalarimiz yoq "})


@api_view(['POST'])
def search_rooms_date(request,pk):
    region = request.POST.get('region')
    date_start = request.POST.get('start').replace('-', '')
    date_end = request.POST.get('end').replace('-', '')
    region = Region.objects.get(pk=pk)
    rooms = Room.objects.filter(hotel__region=region)
    free_rooms = []
    for room in rooms:
        hotel_orders = room.room_order.all()
        dates = []
        xx = True
        for d in range(int(date_start), int(date_end)+1):
            dates.append(d)
        if hotel_orders:
            for hotel_order in hotel_orders:
                ds = str(hotel_order.start).replace('-', '')
                de = str(hotel_order.end).replace('-', '')
                for i in range(int(ds), int(de)+1):
                    if i in dates:
                        xx = False
        if xx == True:
            free_rooms.append(room)
    if len(free_rooms) > 0:
        ser = RoomSerializer(free_rooms, many=True)
        return Response(ser.data)
    else:
        return Response({"message": "bu kunlarga bosh xonalarimiz yoq "})


@api_view(['POST'])
def filter_room_price(request,pk):
    date_start = request.POST.get('start').replace('-', '')
    date_end = request.POST.get('end').replace('-', '')
    price_1 = int(request.POST.get("price_1"))
    price_2 = int(request.POST.get("price_2"))
    region = Region.objects.get(pk=pk)
    rooms = Room.objects.filter(hotel__region=region,price__gte=price_1,price__lt=price_2)
    free_rooms = []
    for room in rooms:
        hotel_orders = room.room_order.all()
        dates = []
        xx = True
        for d in range(int(date_start), int(date_end) + 1):
            dates.append(d)
        if hotel_orders:
            for hotel_order in hotel_orders:
                ds = str(hotel_order.start).replace('-', '')
                de = str(hotel_order.end).replace('-', '')
                for i in range(int(ds), int(de) + 1):
                    if i in dates:
                        xx = False
        if xx == True:
            free_rooms.append(room)
    if len(free_rooms) > 0:
        ser = RoomSerializer(free_rooms, many=True)
        return Response(ser.data)
    else:
        return Response({"message": "bu kunlarga bosh xonalarimiz yoq "})

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_constant(request):
    user = request.user
    hotel = request.POST.get('hotel')
    constant = Constant.objects.create(
        user = user,
        hotel_id = hotel,
        )
    ser = CardSerializer(card)
    return Response(ser.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def constant_view(request):
    user = request.user
    constants = Constant.objects.filter(user=user)
    ser = ConstantSerializer(Constant, many=True)
    return Response(ser.data)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def constant_delete(request,pk):
    constant = Constant.objects.get(pk=pk)
    constant.delete()
    return Response("Deleted succes")


@api_view(['POST'])
def create_comment(request,pk):
    hotel = Hotel.objects.get(pk=pk)
    izox = request.POST['izox']
    comment = Comment.objects.create(
        text=izox,
        user=request.user,
        hotel=hotel,
    )
    ser = CommentSerializer(comment)
    return Response(ser.data)


@api_view(['POST'])
def signin_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usrs = User.objects.get(username=username)
        usr = authenticate(username=username, password=password)
        try:
            if usr is not None:
                status = 200
                token, created = Token.objects.get_or_create(user=usrs)
                data = {
                    'username': username,
                    'user_id': usrs.id,
                    'token': token.key,
                }
            else:
                status = 403
                message = " Username yoki parol noto'g'ri ! "
                data = {
                    'status': status,
                    'message': message,
                }
        except User.DoesNotExist:
            status = 404
            message = ' Bunday foydalanuvchi mavjud emas! '
            data = {
                'status': status,
                'message': message,
            }
        return Response(data)
    except Exception as err:
        return Response(f'{err}')


@api_view(['POST'])
def signup_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    user = User.objects.create_user(username=username, password=password, email=email)
    ser = UserSerializer(user)
    return Response(ser.data)

@api_view(['GET'])
def logout_view(request):
    logout(request)
    return Response("logout")
