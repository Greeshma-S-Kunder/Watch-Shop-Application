from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('upload', views.uploads, name="upload_images"),
    path('login',views.loginn,name="login"),
    path('About',views.About,name="About"),
    path('dummy',views.show_api,name="dummy"),
    path('logout',views.logouts,name="logout"),
    path('product/<int:id>', views.product_view, name="product"),
    path('register',views.register,name="register"),
    path('addWish/<int:id>',views.Wish_list,name="addWish"),
    path('addCart/<int:id>',views.Cart_list,name="addCart"),
    path('ShowWishlist',views.ShowWishlist,name="ShowWishlist"),
    path('show_cartList',views.show_cartList,name="show_cartList"),
    path('ShowWishlist/removewish/<int:id>',views.remove_wish,name="removewish"),
    path('show_cartList/removecart/<int:id>', views.remove_cart_item, name="removecart"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)