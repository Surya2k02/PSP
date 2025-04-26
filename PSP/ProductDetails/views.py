from django.shortcuts import render,redirect,get_object_or_404
from .models import Inventory
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("PSP")  # Change to your home URL name
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "ProductDetails/login.html")

def display (request):
    inventory = Inventory.objects.all()
    return render(request,'ProductDetails/Index.html',{ 'inventory':inventory })

def Addproducts (request):
    return render(request,'ProductDetails/Addproducts.html')

def insertproduct (request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    price = request.POST.get('price')
    stock_qty = request.POST.get('stock_qty')
    category = request.POST.get('category')
    Product = Inventory(name=name,description=description,price=price,stock_qty=stock_qty,category=category)
    Product.save()
    return redirect('/PSP')

def editProducts(request,id):
    product = get_object_or_404 (Inventory, id=id)
    return render(request,'ProductDetails/Updateproducts.html',{'product':product})

def updateProducts(request,id):
    product = get_object_or_404 (Inventory, id=id)
    name = request.POST.get('name')
    description = request.POST.get('description')
    price = request.POST.get('price')
    stock_qty = request.POST.get('stock_qty')
    category = request.POST.get('category')
    product = Inventory.objects.get(id=id)
    product.name = name
    product.description = description
    product.price = price
    product.stock_qty = stock_qty
    product.category = category
    product.save()
    return redirect('/PSP')


def DeleteProduct(request, id):
    product = get_object_or_404 (Inventory, id=id)
    product.delete()
    return redirect('/PSP')

