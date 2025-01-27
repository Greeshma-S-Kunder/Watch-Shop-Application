from django.contrib import admin
from .models import Food
from .models import FoodImages
from .models import Wishlist
from .models import Cart
from .models import FoodReview
from .models import Cartitem

# Register your models here.
admin.site.register(Food)
class FoodUploadAdmin(admin.ModelAdmin):
   list_display=('name','category', 'cost', 'images') 
   fields=['name','category', 'cost', 'images']


admin.site.register(FoodImages, FoodUploadAdmin)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(FoodReview)
admin.site.register(Cartitem)
