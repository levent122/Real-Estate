from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):

    STATUS = (('S','For sale'), ('R','For rent'))
    is_there = (('Y','Yes'), ('N','No'))

    realtor = models.ForeignKey(User, on_delete= models.CASCADE, related_name="realtor")
    title = models.CharField(max_length= 200)
    address = models.TextField()
    city = models.CharField(max_length= 100)
    district = models.CharField(max_length= 100)
    description = models.TextField()
    status = models.CharField(max_length= 1, choices= STATUS)
    price = models.IntegerField()
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    garage = models.IntegerField()
    sqft = models.FloatField()
    product_age = models.FloatField()
    air_conditioning = models.CharField(max_length= 1, choices= is_there)
    central_heating = models.CharField(max_length= 1, choices= is_there)
    city_views = models.CharField(max_length= 1, choices= is_there)
    telephone = models.CharField(max_length= 1, choices= is_there)
    internet = models.CharField(max_length= 1, choices= is_there)
    laundry_room = models.CharField(max_length= 1, choices= is_there)
    metro_central = models.CharField(max_length= 1, choices= is_there)
    electric_range = models.CharField(max_length= 1, choices= is_there)
    video = models.ImageField(blank=True)
    photo_main = models.ImageField()
    photo_1 = models.ImageField()
    photo_2 = models.ImageField()
    photo_3 = models.ImageField()
    photo_4 = models.ImageField()
    photo_5 = models.ImageField(blank=True)
    photo_6 = models.ImageField(blank=True)
    photo_7 = models.ImageField(blank=True)
    photo_8 = models.ImageField(blank=True)
    photo_9 = models.ImageField(blank=True)
    photo_10 = models.ImageField(blank=True)
    published_date = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.title





