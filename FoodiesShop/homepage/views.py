from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
#here the upload can not be opened unless we login into our admin account - decorator
from django.contrib.auth.decorators import login_required
from .models import FoodImages, Wishlist, Cart, FoodReview, Cartitem
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, logout, login
from .forms import UploadForms
from django.http import JsonResponse


def Home(request):
    Foods=FoodImages.objects.all()
    context={'Food':Foods}
    return render(request,"Home.html", context)



def products(request, id):
    product=get_object_or_404(FoodImages, id=id)
    return render(request,"product.html", {'product':product})

def About(request):
    return render(request,"About.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the user with a hashed password
        return redirect('login')  # Redirect to login page after successful registration   
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def show_api(request):
    start_text=request.GET.get('parameter1')
    FoodName=FoodImages.objects.filter(name__startswith=start_text).first()
    if FoodName:
        message={
            "FoodName":FoodName.name,
            "name":"Hey, this is my data"
        }
    else:
        message={
            "name":"data not foundd"
        }
    return JsonResponse(message)



def logouts(request):
    logout(request) 
    return redirect('home')

@login_required(login_url="/login")
def uploads(request):
    if request.method == 'POST':
        form = UploadForms(request.POST, request.FILES)
        print(request.FILES)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =UploadForms()
        images=FoodImages.objects.all()

    return render(request, 'uploads.html', {'form':form})
 


def product_view(request, id):
    product = get_object_or_404(FoodImages, id=id)
    review_obj = FoodReview.objects.filter(product=product)
    
    return render(request, 'product.html', {'product': product, "review_obj": review_obj})




def Wish_list(request, id):
    product = FoodImages.objects.get(id=id)
    obj1, created =Wishlist.objects.get_or_create(user=request.user)
    obj1.product.add(product)
    obj1.save()
    return redirect('home')



def ShowWishlist(request):
    user = request.user
    wishlist_items = Wishlist.objects.filter(user=user).prefetch_related('product')
    products=[]
    for wishlist in wishlist_items:
        for product in wishlist.product.all():

            products.append({
               'product':product, 
               'wishlist_id':wishlist.id 
            })
    
    return render(request, 'wishlist.html', {'view_products': products})





def Cart_list(request, id):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    product = FoodImages.objects.get(id=id)

    # Check if the item already exists in the cart
    cart_item, created = Cartitem.objects.get_or_create(cart=user_cart, product=product)
    if not created:
        # If it already exists, increase the quantity
        cart_item.cart_count += 1
    cart_item.save()

    return redirect('home')





def show_cartList(request):
    cart, created=Cart.objects.get_or_create(user=request.user)
    cart_items=Cartitem.objects.filter(cart = cart)
    return render(request, "CartList.html", {"user_products":cart_items})




def loginn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


    
def remove_wish(request, id):
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user).first()  # Get user's wishlist

        if wishlist:
            product = FoodImages.objects.get(id=id)  # Get the specific product
            wishlist.product.remove(product)  # Remove only this product from the wishlist

            # If wishlist is empty after removal, you can optionally delete it
            if wishlist.product.count() == 0:
                wishlist.delete()

        return redirect('ShowWishlist')
    else:
        return redirect('login')


    
def remove_cart_item(request, id):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        product = get_object_or_404(FoodImages, id=id)

        # Remove the selected product from the cart entirely
        cart_item = Cartitem.objects.filter(cart=cart, product=product).first()
        if cart_item:
            cart_item.delete()  # Completely remove the item

        return redirect('show_cartList')
    else:
        return redirect('login')




