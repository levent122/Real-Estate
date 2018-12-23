from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from product.models import Product

class UserInfo(models.Model):

    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="user_info")
    photo = models.ImageField(default=  'download.jpg')
    birthday = models.DateTimeField(blank=True, null=True)
    web = models.CharField(blank=True, null=True,max_length= 100)
    description = models.TextField(blank=True, null=True)
    instagram = models.CharField(blank=True, null=True,max_length= 100)
    twitter = models.CharField(blank=True, null=True,max_length= 100)
    facebook = models.CharField(blank=True, null=True,max_length= 100)
    phone = models.CharField(blank=True, null=True,max_length= 20)
    def __str__(self):
        return self.user.username

def create_user_info(instance,created,**kwargs):
    if created:
        UserInfo.objects.create(user= instance)

post_save.connect(receiver=create_user_info,sender=User)



class Like(models.Model):

    user = models.ForeignKey('auth.User', on_delete= models.CASCADE, related_name='like')
    product = models.ForeignKey(Product, on_delete= models.DO_NOTHING, related_name='liked_product')
    date = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return '%s'%(self.product)