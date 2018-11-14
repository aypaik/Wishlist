from django.shortcuts import render, redirect
from ..login_app.models import User
from models import Product
# Create your views here.
def dashboard(request):
    context = {
        'cur_user': User.objects.get(id = request.session['id']),
        'user_products': Product.objects.filter(wishlist = request.session['id']),
        'other_products': Product.objects.exclude(wishlist = request.session['id']),
    }
    return render(request, 'main_app/dashboard.html', context)

def add(request):
    return render(request, 'main_app/add.html')

def create(request):
    logged_user = User.objects.get(id = request.session['id'])
    new_product = Product.objects.create(
        product_name = request.POST['product_name'],
        created_by = User.objects.get(id=request.session['id'])
    )
    User.objects.get(id = request.session['id']).items_made.add(new_product)
    User.objects.get(id = request.session['id']).wishlist.add(new_product)
    return redirect('/main/dashboard')

def removefromlist (request, id):
    item = Product.objects.get(id = id)
    user = User.objects.get(id = request.session['id'])
    user.wishlist.remove(item)
    return redirect('/main/dashboard')

def addtolist (request, id):
    item = Product.objects.get(id = id)
    user = User.objects.get(id = request.session['id'])
    user.wishlist.add(item)
    return redirect('/main/dashboard')

def show(request, id):
    context = {
        'product': Product.objects.get(id = id)
    }
    return render(request, 'main_app/show.html', context)