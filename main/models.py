from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/', blank=True, null=True)


    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'



class Photo(models.Model):
    img=models.ImageField(upload_to='photos/')


class Advantages(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Region(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    photo = models.ManyToManyField(Photo,blank=True)
    phone = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    map_lot = models.CharField(max_length=255)
    map_long = models.CharField(max_length=255)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    rating = models.IntegerField()
    in_slider = models.BooleanField(default=False)
    adventages = models.ManyToManyField(Advantages,blank=True)
    is_active = models.BooleanField(default=True)
    center = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    number = models.IntegerField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=255)
    photo = models.ManyToManyField(Photo,blank=True)
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    price = models.IntegerField()
    room_type = models.IntegerField(default=1, choices=(
        (1, 'econom'),
        (2, 'lux'),
    ))
    in_slider = models.BooleanField(default=False)
    adventages = models.ManyToManyField(Advantages,blank=True)
    is_active = models.BooleanField(default=True)
    status = models.IntegerField(default=1, choices=(
        (1, 'Free'),
        (2, 'busy'),
    ))
    date = models.DateTimeField(auto_now=True)




class Hotel_order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    pas_photo = models.ImageField(upload_to='passport_photos/')
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_order')
    email = models.CharField(max_length=255)


class Comment(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Constant(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
