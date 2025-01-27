from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()

    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)


class FoodImages(models.Model):
    name=models.CharField(max_length=100)
    category=models.TextField()
    cost=models.FloatField()
    images=models.ImageField(upload_to='food/')
    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(FoodImages)
    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)

class Cartitem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(FoodImages, on_delete=models.CASCADE)
    cart_count=models.IntegerField(default=1)
    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)

class FoodReview(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    product= models.ForeignKey(FoodImages, on_delete=models.CASCADE)
    review_text=models.TextField()
    rating= models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1,6)])
    updated= models.DateTimeField(auto_now=True)
    created= models.DateTimeField(auto_now_add=True)
